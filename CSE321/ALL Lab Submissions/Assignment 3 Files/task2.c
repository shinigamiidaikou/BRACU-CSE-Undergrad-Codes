#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/wait.h>

#define MSG_LOGIN_TO_OTP 1
#define MSG_OTP_TO_LOGIN 2
#define MSG_OTP_TO_MAIL 3
#define MSG_MAIL_TO_LOGIN 4

struct msg
{
    long type;
    char txt[6];
};

int main()
{
    key_t key = ftok("msgqueue", 65);
    int msgid = msgget(key, 0666 | IPC_CREAT);
    if (msgid == -1)
    {
        perror("msgget");
        exit(1);
    }

    struct msg message, otp_message, mail_message;
    printf("Please enter the workspace name:\n");
    scanf("%s", message.txt);

    if (strcmp(message.txt, "cse321") != 0)
    {
        printf("Invalid workspace name\n");
        msgctl(msgid, IPC_RMID, NULL);
        exit(0);
    }

    pid_t pid1 = fork();

    if (pid1 > 0)
    {
        message.type = MSG_LOGIN_TO_OTP;
        if (msgsnd(msgid, &message, sizeof(message.txt), 0) == -1)
        {
            perror("msgsnd");
            exit(1);
        }
        printf("Workspace name sent to OTP generator from log in: %s\n", message.txt);

        if (msgrcv(msgid, &otp_message, sizeof(otp_message.txt), MSG_OTP_TO_LOGIN, 0) == -1)
        {
            perror("msgrcv");
            exit(1);
        }
        printf("Log in received OTP from OTP generator: %s\n", otp_message.txt);

        if (msgrcv(msgid, &mail_message, sizeof(mail_message.txt), MSG_MAIL_TO_LOGIN, 0) == -1)
        {
            perror("msgrcv");
            exit(1);
        }
        printf("Log in received OTP from mail: %s\n", mail_message.txt);

        if (strcmp(otp_message.txt, mail_message.txt) == 0)
        {
            printf("OTP Verified\n");
        }
        else
        {
            printf("OTP Incorrect\n");
        }

        wait(NULL);
        msgctl(msgid, IPC_RMID, NULL);
    }
    else
    {
        struct msg received_message, otp_message;

        if (msgrcv(msgid, &received_message, sizeof(received_message.txt), MSG_LOGIN_TO_OTP, 0) == -1)
        {
            perror("msgrcv");
            exit(1);
        }
        printf("OTP generator received workspace name from log in: %s\n", received_message.txt);

        pid_t otp = getpid();
        sprintf(otp_message.txt, "%d", otp);

        otp_message.type = MSG_OTP_TO_LOGIN;
        msgsnd(msgid, &otp_message, sizeof(otp_message.txt), 0);
        printf("OTP sent to log in from OTP generator: %s\n", otp_message.txt);

        otp_message.type = MSG_OTP_TO_MAIL;
        msgsnd(msgid, &otp_message, sizeof(otp_message.txt), 0);
        printf("OTP sent to mail from OTP generator: %s\n", otp_message.txt);

        pid_t pid2 = fork();
        if (pid2 == 0)
        {
            struct msg mail_message;
            if (msgrcv(msgid, &mail_message, sizeof(mail_message.txt), MSG_OTP_TO_MAIL, 0) == -1)
            {
                perror("msgrcv");
                exit(1);
            }
            printf("Mail received OTP from OTP generator: %s\n", mail_message.txt);

            mail_message.type = MSG_MAIL_TO_LOGIN;
            msgsnd(msgid, &mail_message, sizeof(mail_message.txt), 0);
            printf("OTP sent to log in from mail: %s\n", mail_message.txt);
            exit(0);
        }

        wait(NULL);
        exit(0);
    }

    return 0;
}
