#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void main()
{
	int pid, status;
	pid = fork();
	if(pid == -1) {
		printf("fork failed\n");
		exit(1);
	}
	if(pid == 0) {
		/* Child */
		printf("Child here!\n");
	}
	else {
		/* Parent */
		wait(&status);
		printf("Well done kid!\n");
	}
}
