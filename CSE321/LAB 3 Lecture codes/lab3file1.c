#include <stdio.h>

int main () {
	FILE *fp;
	char buff[255];
	
	fp = fopen("in.txt", "r");
	
	//fscanf(fp, "%s", buff);
	//printf("Contents in in.txt: %s\n", buff);
	
	fgets(buff, 255, fp);
	printf("Contents in in.txt: %s\n", buff);
	
	fclose(fp);
}
