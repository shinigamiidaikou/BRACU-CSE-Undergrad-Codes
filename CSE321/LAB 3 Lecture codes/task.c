#include <stdio.h>

int main () {
	char str[100];
	
	printf("Enter string: ");
	scanf("%[^\n]", str);
	
	char *ip = str;
	
	int count = 0;
	
	while (*ip != '\0') {
		count++;
		ip++;
	}
	printf("%d\n", count);
}
