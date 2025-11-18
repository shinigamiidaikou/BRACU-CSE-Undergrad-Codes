#include <stdio.h>
#include <pthread.h>
#include <string.h>

int name_sums[3] = {0};

int calculate_ascii_sum(const char* name) {
    int sum = 0;
    for(int i = 0; name[i] != '\0'; i++) {
        sum += (int)name[i];
    }
    return sum;
}

void* process_name(void* arg) {
    char* name = (char*)arg;
    int thread_id = name_sums[0] == 0 ? 0 : (name_sums[1] == 0 ? 1 : 2);
    name_sums[thread_id] = calculate_ascii_sum(name);
    pthread_exit(NULL);
}

void* check_results(void* arg) {
    if(name_sums[0] == name_sums[1] && name_sums[1] == name_sums[2]) {
        printf("Youreka\n");
    }
    else if(name_sums[0] == name_sums[1] || name_sums[1] == name_sums[2] || 
            name_sums[0] == name_sums[2]) {
        printf("Miracle\n");
    }
    else {
        printf("Hasta la vista\n");
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[4];
    char name1[] = "Alice";
    char name2[] = "Bob";
    char name3[] = "Charlie";
    
    pthread_create(&threads[0], NULL, process_name, name1);
    pthread_create(&threads[1], NULL, process_name, name2);
    pthread_create(&threads[2], NULL, process_name, name3);
    
    for(int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }
    
    pthread_create(&threads[3], NULL, check_results, NULL);
    pthread_join(threads[3], NULL);
    
    return 0;
}
