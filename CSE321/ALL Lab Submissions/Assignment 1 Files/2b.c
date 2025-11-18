#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE *in = fopen("input.txt", "r");
    FILE *out = fopen("output.txt", "w");

    if (in == NULL || out == NULL)
    {
        printf("Error opening file(s)!\n");
        return 0;
    }

    char *line = NULL;
    size_t len = 0;
    const char *delim = " ";

    while (getline(&line, &len, in) != -1)
    {
        char *token = strtok(line, delim);
        int first_word = 1;

        while (token != NULL)
        {
            if (!first_word)
            {
                fprintf(out, " ");
            }
            fprintf(out, "%s", token);
            first_word = 0;
            token = strtok(NULL, delim);
        }
        fprintf(out, "\n");
    }

    free(line);
    fclose(in);
    fclose(out);

    printf("Extra spaces removed and written to output.txt\n");
    return 0;
}
