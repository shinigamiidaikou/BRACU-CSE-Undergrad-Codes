#include<stdio.h> // standard i/o
#include<fcntl.h> // file control
#include<unistd.h> // unit standard

int main() {
	int fd;
	char buffer[80];
	static char message[] = "Hello, world! My name is Shafin Ahmed.";
	fd = open("myfile.txt",O_RDWR);
	if (fd != -1) {
		printf("myfile.txt opened for read/write access.\n");
		write(fd, message, sizeof(message));
		lseek(fd, 0, 0); /* go back to the beginning of the file */
		read(fd, buffer, sizeof(message));
		printf("\"%s\" was written to myfile.txt.\n", buffer);
		close (fd);
	} else {
		printf("myfile.txt failed to access.\n");
	}
	return 0;
}
