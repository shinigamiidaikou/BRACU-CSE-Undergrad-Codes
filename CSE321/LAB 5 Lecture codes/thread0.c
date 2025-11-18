#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *foo(void *arg) {
	printf("in foo: foo begins\n");
	sleep(1);
	printf("in foo: foo ENDS\n");
}

int main () {
	printf("in main: main begins\n");
	// foo(NULL);
	
	pthread_t t1;
	pthread_create(&t1, NULL, foo, NULL);

	pthread_join(t1, NULL);

	printf("in main: a random line after foo\n");
	
	// pthread_join(t1, NULL);
	
	printf("in main: main ENDS\n");

	// pthread_join(t1, NULL);
		
	return 0;
}
