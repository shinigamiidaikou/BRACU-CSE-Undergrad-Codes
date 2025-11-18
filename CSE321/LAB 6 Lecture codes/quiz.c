#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/shm.h>
#include <sys/ipc.h>

int main()
{

	int fd[2], fd1[2];
	pid_t a;

	char message[200];

	int pipe_1 = pipe(fd);
	int pipe_2 = pipe(fd1);

	a = fork();

	if (a != 0)
	{
		close(fd[1]);
		close(fd1[0]);

		printf("Enter Message for check:\n");
		read(0, message, sizeof(message));

		printf("Writing data for sending in child\n");
		write(fd1[1], message, sizeof(message));
		printf("Writing to child done\n");

		printf("Reading data after receiving from child\n");
		read(fd[0], message, sizeof(message));
		printf("Data received from child: %s\n", message);
		close(fd1[1]);
		close(fd[0]);
		
	}
	else
	{

		close(fd[0]);
		close(fd1[1]);

		char* check = "CSE321";

		printf("Reading data after receiving from parent\n");
		read(fd1[0], message, sizeof(message));
		printf("Data received from parent: %s\n", message);

		if (strcmp(message, check))
		{
			write(fd[1], "Matched", 7);
		}
		else
			write(fd[1], "Not Matched", 11);

		close(fd1[0]);
		close(fd[1]);
	}

	return 0;
}