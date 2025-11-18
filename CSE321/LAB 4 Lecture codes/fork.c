#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

void main()
{
	pid_t pid;
	pid = fork();
	if (pid == 0)
		printf("\nI'm the child process\n");
	else if (pid > 0)
		printf("\nI'm the parent process. My child pid is %d\n", pid);
	else
		perror("error in fork");
}
