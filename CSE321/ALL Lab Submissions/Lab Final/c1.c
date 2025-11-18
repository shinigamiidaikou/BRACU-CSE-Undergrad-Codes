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

int main () {
	int a;
	printf("Enter value of n (Odd): ");
	scanf("%d", &a);
	
	for (int i = 0; i < a; i++) {
		for (int j = 0; j < 2*i+1; j++){
			printf("*");
		}
		printf("\n");
	}
	
	for (int j = 0; j < 2 * a + 1; j++){
		printf("*");
	}
	printf("\n");

	for (int i = a-1; i >= 0; i--) {
		for (int j = 0; j < 2*i+1; j++){
			printf("*");	
		}
		printf("\n");
	}

	return 0;
}

