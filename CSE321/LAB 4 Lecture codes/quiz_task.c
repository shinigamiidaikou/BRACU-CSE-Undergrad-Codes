#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int c1 = fork();
    if ( c1 == 0 ) {
        int c2 = fork();
        if ( c2 == 0 ) {
            int c3 = fork();
            if ( c3 == 0 ) printf("gcc\n");
	    else {
                wait(NULL);
                printf("gc\n");
	    }
        }else {
            wait(NULL);
            printf("c\n");
	}
    }else {
    	wait(NULL);
    	printf("p\n");
    }
    return 0;
}
