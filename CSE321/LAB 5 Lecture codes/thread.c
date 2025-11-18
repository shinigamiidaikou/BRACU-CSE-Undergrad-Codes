#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void *foo(void *arg) {
	printf("in foo: foo begins\n");
	sleep(1);
	printf("in foo: foo ENDS\n");
}

int main () {
	printf("in main: main begins\n");
	foo(NULL);
	printf("in main: a random line after foo\n");
	printf("in main: main ENDS\n");
	
	return 0;
}
