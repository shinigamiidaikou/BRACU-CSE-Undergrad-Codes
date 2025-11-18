#include <stdio.h>
#include <string.h>
#include <ctype.h>

void validate_password(const char *password) {
    int has_lower = 0, has_upper = 0, has_digit = 0, has_special = 0;
    for (int i = 0; i < strlen(password); i++) {
        if (islower(password[i])) has_lower = 1;
        else if (isupper(password[i])) has_upper = 1;
        else if (isdigit(password[i])) has_digit = 1;
        else if (strchr("_$#@", password[i])) has_special = 1;
    }
    int first_missing = 1;
    if (has_lower && has_upper && has_digit && has_special){
        printf("OK\n");
    } else {
        if (!has_lower) {
            printf("Lowercase character missing");
            first_missing = 0;
        }
        if (!has_upper) {
            if (first_missing) {
                printf("Uppercase character missing");
                first_missing = 0;
            } else printf(", Uppercase character missing");
        }
        if (!has_digit) {
            if (first_missing) {
                printf("Digit missing");
                first_missing = 0;
            } else printf(", Digit missing");
        }
        if (!has_special) {
            if (first_missing) {
                printf("Special character missing");
                first_missing = 0;
            } else printf(", Special character missing");
        }
        printf("\n");
    }
}

int main() {
    char password[50];
    printf("Enter password: ");
    scanf("%s", password);
    validate_password(password);
    return 0;
}
