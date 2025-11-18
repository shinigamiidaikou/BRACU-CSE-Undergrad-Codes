#include <stdio.h>

int isPerfect(int num) {
    int sum = 1;
    
    for(int i = 2; i * i <= num; i++) {
        if(num % i == 0) {
            sum += i;
            if(i * i != num) {
                sum += num / i;
            }
        }
    }
    
    return (sum == num && num != 1);
}

int main() {
    int start, end;
    
    scanf("%d", &start);
    scanf("%d", &end);
    
    for(int i = start; i <= end; i++) {
        if(isPerfect(i)) {
            printf("%d\n", i);
        }
    }

    return 0;
}
