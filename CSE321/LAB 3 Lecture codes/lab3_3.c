#include <stdio.h>
#include <string.h>

struct Student {
	long id;
	char name[100];
	float cgpa;
};

int main() {
	struct Student shafin;
	shafin.id = 22101621;
	strcpy(shafin.name, "Shafin Ahmed");
	shafin.cgpa = 3.9564;
	
	printf("ID = %ld\n", shafin.id);
	printf("Name = %s\n", shafin.name);
	printf("CGPA = %.2f\n", shafin.cgpa);
	
	return 0;
}
