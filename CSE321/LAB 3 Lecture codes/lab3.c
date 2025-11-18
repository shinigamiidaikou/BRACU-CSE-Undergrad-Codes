#include <stdio.h>
#include <string.h>

int main(){
    char str1[50] = "Name: ";
    char *str2 = "Shafin Ahmed";

    printf("%s\n",str1);
    printf("%s\n",str2);
    
    strcat(str1, str2);

    printf("%s\n",str1);
    printf("%s\n",str2);

	printf("===================\n");
	        
    strcpy(str1, str2);
    
    printf("%s\n",str1);
    printf("%s\n",str2);
    
    printf("===================\n");
    
    char strn_1[100] = {'h','o','l','y','\0'};
    printf("%s has the size %ld\n", strn_1, strlen(strn_1));
    
    char strn_2[100] = {'h','o','l','a'};
    printf("%s has the size %ld\n", strn_2, strlen(strn_2));
    
    printf("%d\n", strcmp(strn_1, strn_2));
    
    printf("===================\n");
    
    char c='a', d='y';
    printf("%d\n", c);
    printf("%d\n", d);
    printf("%d\n", c-d);

    return 0;
}
