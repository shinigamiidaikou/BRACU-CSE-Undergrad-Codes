#include <stdio.h>

void func(int x){
	x = 10;
	printf("from func: x = %d\n",x);
}

void funcdrf(int *x){
	*x = 10; // dereferecing and assigning
	printf("from func: x = %d\n",*x);
}

int main(){
	int x = 6;
	printf("from main before func call, x = %d\n", x);
	func(x); //value passing
	printf("from main before func call, x = %d\n", x);
	
	printf("from main before funcdrf call, x = %d\n", x);
	funcdrf(&x); // reference passing
	printf("from main before funcdrf call, x = %d\n", x);
	
	return 0;
}
