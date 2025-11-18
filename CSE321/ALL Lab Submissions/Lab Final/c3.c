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
#include <semaphore.h>

char alphas[3] = {'a','b','c'};
void *print_funca(char *alph);
void *print_funcb(char *alph);
void *print_funcc(char *alph);

sem_t s;

int main () {
	pthread_t t[3];
	sem_init(&s, 0, 1);
	
	pthread_create(&t[0], NULL, (void *)print_funca, &alphas[0]);
	pthread_create(&t[1], NULL, (void *)print_funcb, &alphas[1]);
	pthread_create(&t[2], NULL, (void *)print_funcc, &alphas[2]);
	for (int i = 0; i < 3; i++){
		pthread_join(t[i], NULL);
	}
	printf("\n");
	
	sem_destroy(&s);
	return 0;
}


void *print_funca(char *alph) {
	for (int i = 0; i < 20; i++){
		printf("%c", *alph);
		sem_wait(&s);
	}
}

void *print_funcb(char *alph) {
	for (int i = 0; i < 20; i++){
		sem_post(&s);
		printf("%c", *alph);
		sem_wait(&s);
	}
}

void *print_funcc(char *alph) {
	for (int i = 0; i < 20; i++){
		sem_post(&s);
		printf("%c", *alph);
		sem_wait(&s);
	}
}
