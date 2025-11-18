#include <stdio.h>
#include <pthread.h>

void* print_numbers(void* arg) {
    int thread_id = *(int*)arg;
    int start_num = (thread_id * 5) + 1;
    
    for(int i = 0; i < 5; i++) {
        printf("Thread %d prints %d\n", thread_id, start_num + i);
    }
    
    pthread_exit(NULL);
}

int main() {
    pthread_t thread;
    int thread_ids[5];
    
    for(int i = 0; i < 5; i++) {
        thread_ids[i] = i;
        pthread_create(&thread, NULL, print_numbers, &thread_ids[i]);
        pthread_join(thread, NULL);
    }
    
    return 0;
}
