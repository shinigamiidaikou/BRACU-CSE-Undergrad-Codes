#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/file.h>
#include <sys/stat.h>
#include <pthread.h>

int a;
char buff[] = "Bug fix log, each number represents the bugs fixed in a commit.\n";

int main () {	
	
	FILE *fp = fopen("bug_fix_log.txt", "w");
	
	fprintf(fp, "%s", buff);
	
	pid_t pid;
	
	pid = fork();
	if (pid == 0){
		printf("Enter commit for (1): ");
		scanf("%d", &a);
		fprintf(fp, "%d ", a);
		exit(0);
	} else wait(NULL);
	
	pid = fork();
	if (pid == 0){
		printf("Enter commit for (2): ");
		scanf("%d", &a);
		fprintf(fp, "%d\n", a);
		exit(0);
	} else wait(NULL);

	
	fclose(fp);
	
	//FILE *fp1 = fopen("buf_fix_log.txt", "r");
	//fclose(fp1);

	return 0;
}

