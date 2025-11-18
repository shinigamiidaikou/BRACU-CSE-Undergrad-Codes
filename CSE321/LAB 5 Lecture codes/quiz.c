#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *task1 (void *arg1);
void *task2 (void *arg2);
void *task3 (void *arg3);
void *t_ret;

int num;

int main () {

	printf("Enter Number: ");
	scanf("%d", &num);
	
	pthread_t t1;
	pthread_t t2;
	pthread_t t3;
	pthread_create(&t1, NULL, (void *)task1, &num);
	pthread_join(t1, &t_ret);
	num = *t_ret;
	pthread_create(&t2, NULL, (void *)task2, &num);
	pthread_join(t2, &t_ret);
	num = *t_ret;
	pthread_create(&t3, NULL, (void *)task3, &num);
	pthread_join(t3, &t_ret);
	num = *t_ret;
	
	printf("The solve of equation: %d\n", num);
	return 0;
}

void *task1 (void *arg1){
	int num = *arg1
	num = num - 2;
	pthread_exit(num);
}

void *task2 (void *arg2){
	int num = *arg1
	num = num * 3;
	pthread_exit(num);
}

void *task3 (void *arg3){
	int num = *arg1
	num = num + 1;
	pthread_exit(num);
}

