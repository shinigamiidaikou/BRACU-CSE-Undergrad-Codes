#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

int count = 0;

pthread_mutex_t mutex;

void *func_to_run(void *arg)
{
    for (int i = 0; i < 1000000; i++)
    {
        pthread_mutex_lock(&mutex);

        count += 1;

        pthread_mutex_unlock(&mutex);
    }
}

int main()
{
    int tc = 4;
    pthread_t t[tc];

    pthread_mutex_init(&mutex, NULL);
    for (int i = 0; i < tc; i++)
    {
        pthread_create(&t[i], NULL, (void *)func_to_run, NULL);
    }

    for (int i = 0; i < tc; i++)
    {
        pthread_join(t[i], NULL);
    }
    pthread_mutex_destroy(&mutex);

    printf("count = %d\n", count);

    return 0;
}