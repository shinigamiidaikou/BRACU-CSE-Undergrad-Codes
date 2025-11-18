#include<stdio.h>
#include<unistd.h>

int main(){
	printf("exec_program Running...\n");
	pid_t pid, status;
	pid = fork();
	if(pid == 0)
		execl("/home/ubuntu/Documents/CSE321 Lab 4/program1", "a", "b", "c", "d", NULL);
	else if(pid>0){
		wait(&status);
		execl("bin/pwd/","pwd", NULL);
	}
	return 0;
}
