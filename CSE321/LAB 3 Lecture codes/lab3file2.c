#include <stdio.h>

int main () {
	FILE *fp;
	char buff[255];
	
	fp = fopen("out.txt", "w+");
	
	fputs("Hello World\n", fp);
	
	fclose(fp);
}
