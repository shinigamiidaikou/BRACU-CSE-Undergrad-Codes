#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <sys/file.h>

void increment_count() {
    int fd = open("count.txt", O_RDWR | O_CREAT, 0644);
    if (fd == -1) return;
    
    flock(fd, LOCK_EX);
    
    char buf[10] = {0};
    int count = 1;
    
    lseek(fd, 0, SEEK_SET);
    if (read(fd, buf, sizeof(buf)) > 0) {
        count = atoi(buf) + 1;
    }
    
    lseek(fd, 0, SEEK_SET);
    sprintf(buf, "%d", count);
    write(fd, buf, strlen(buf));
    
    flock(fd, LOCK_UN);
    close(fd);
}

int main() {
    pid_t original_parent = getpid();
    pid_t a, b, c, extra_child;
    
    int fd = open("count.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    write(fd, "1", 1);
    close(fd);

    a = fork();
    if (a >= 0) increment_count();
    
    b = fork();
    if (b >= 0) increment_count();
    
    c = fork();
    if (c >= 0) increment_count();

    if (getpid() % 2 != 0) {
        extra_child = fork();
        if (extra_child >= 0) increment_count();
    }

    if (getpid() == original_parent) {
        while (wait(NULL) > 0);
        fd = open("count.txt", O_RDONLY);
        char buf[10];
        read(fd, buf, sizeof(buf));
        printf("Total number of processes created: %s\n", buf);
        close(fd);
        unlink("count.txt");
    }

    return 0;
}
