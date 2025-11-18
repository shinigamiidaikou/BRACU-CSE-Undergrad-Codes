#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main()
{
    pid_t pid, cpid1, cpid2, cpid3;
    int status;

    printf("1. Parent process ID: 0\n");

    pid = fork();

    if (pid == 0)
    {
        printf("2. Child process ID: %d\n", getpid());

        cpid1 = fork();
        if (cpid1 == 0)
        {
            printf("3. Grand Child process ID: %d\n", getpid());
            exit(0);
        }

        cpid2 = fork();
        if (cpid2 == 0)
        {
            printf("4. Grand Child process ID: %d\n", getpid());
            exit(0);
        }

        cpid3 = fork();
        if (cpid3 == 0)
        {
            printf("5. Grand Child process ID: %d\n", getpid());
            exit(0);
        }

        while (wait(&status) > 0)
            ;
        exit(0);
    }
    else
    {
        wait(&status);
    }

    return 0;
}