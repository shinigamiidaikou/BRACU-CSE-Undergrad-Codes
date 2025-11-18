// Task 1:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>

struct shared
{
    char sel[100];
    int b;
};

int main()
{
    key_t key = ftok("shmfile", 65);
    int shmid = shmget(key, sizeof(struct shared), 0666 | IPC_CREAT);
    struct shared *shm = (struct shared *)shmat(shmid, NULL, 0);

    int pipefd[2];
    if (pipe(pipefd) == -1)
    {
        perror("pipe");
        exit(1);
    }

    printf("Provide Your Input From Given Options:\n");
    printf("1. Type a to Add Money\n2. Type w to Withdraw Money\n3. Type c to Check Balance\n");

    scanf(" %s", shm->sel);
    shm->b = 1000;
    printf("Your selection: %s\n", shm->sel);

    pid_t pid = fork();

    if (pid > 0)
    {
        close(pipefd[1]);

        wait(NULL);

        char buffer[100];
        read(pipefd[0], buffer, sizeof(buffer));
        printf("%s\n", buffer);

        close(pipefd[0]);
        shmdt(shm);
        shmctl(shmid, IPC_RMID, NULL);
    }
    else if (pid == 0)
    {
        close(pipefd[0]);

        if (strcmp(shm->sel, "a") == 0)
        {
            int amount;
            printf("Enter amount to be added:\n");
            scanf("%d", &amount);
            if (amount > 0)
            {
                shm->b += amount;
                printf("Balance added successfully\n");
                printf("Updated balance after addition: %d\n", shm->b);
            }
            else
            {
                printf("Adding failed, Invalid amount\n");
            }
        }
        else if (strcmp(shm->sel, "w") == 0)
        {
            int amount;
            printf("Enter amount to be withdrawn:\n");
            scanf("%d", &amount);
            if (amount > 0 && amount <= shm->b)
            {
                shm->b -= amount;
                printf("Balance withdrawn successfully\nUpdated balance after withdrawal: %d\n", shm->b);
            }
            else
            {
                printf("Withdrawal failed, Invalid amount\n");
            }
        }
        else if (strcmp(shm->sel, "c") == 0)
        {
            printf("Your current balance is: %d\n", shm->b);
        }
        else
        {
            printf("Invalid selection\n");
        }

        write(pipefd[1], "Thank you for using\0", 20);
        close(pipefd[1]);
        shmdt(shm);
        exit(0);
    }

    return 0;
}
