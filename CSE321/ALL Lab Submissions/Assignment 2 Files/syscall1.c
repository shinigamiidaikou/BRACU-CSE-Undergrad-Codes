#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define BUFFER_SIZE 1000

int main(int argc, char *argv[]) {
    int fd;
    char buffer[BUFFER_SIZE];
    char newline = '\n';
    ssize_t bytes_read;

    if (argc != 2) {
        write(0, "Filename not found! Code exit!\n", 31);
        exit(1);
    }

    fd = open(argv[1], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        write(0, "Error opening file!\n", 20);
        exit(1);
    }

    while (1) {
        write(0, "Enter a string (or -1 to exit): ", 32);
        
        bytes_read = read(0, buffer, BUFFER_SIZE);
        if (bytes_read > 0) {
            if (buffer[bytes_read - 1] == '\n') {
                buffer[bytes_read - 1] = '\0';
                bytes_read--;
            }

            if (strcmp(buffer, "-1") == 0) {
                break;
            }

            write(fd, buffer, bytes_read);
        }
    }

    close(fd);
    return 0;
}
