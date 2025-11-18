#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
/*
This program provides a possible solution using mutex and semaphore.
use 5 Farmers and 5 ShopOwners to demonstrate the solution.
*/
#define MaxCrops 5      // Maximum crops a Farmer can produce or a Shpoowner can take
#define warehouseSize 5 // Size of the warehouse
sem_t empty;
sem_t full;
int in = 0;
int out = 0;
char crops[warehouseSize] = {'R', 'W', 'P', 'S', 'M'};     // indicating room for different crops
char warehouse[warehouseSize] = {'N', 'N', 'N', 'N', 'N'}; // initially all the room is empty
pthread_mutex_t mutex;

void *Farmer(void *far)
{   
    int id = *(int *)far;
    for (int k = 0; k < MaxCrops; k++)
    {
        sem_wait(&empty);
        pthread_mutex_lock(&mutex);

        int room = k % warehouseSize;
        warehouse[room] = crops[room];
        printf("Farmer %d: Insert crops %c at %d\n", id, crops[room], room);

        pthread_mutex_unlock(&mutex);
        sem_post(&full);

        printf("Warehouse: ");
        for (int m = 0; m < warehouseSize; m++)
        {
            printf("%c ", warehouse[m]);
        }
        printf("\n");

    }
    return NULL;
}

void *ShopOwner(void *sho)
{
    int id = *(int *)sho;
    for (int k = 0; k < MaxCrops; k++)
    {
        sem_wait(&full);
        pthread_mutex_lock(&mutex);

        int room = k % warehouseSize;
        char item = warehouse[room];
        warehouse[room] = 'N';
        printf("ShopOwner %d: Remove crops %c from %d\n", id, item, room);

        pthread_mutex_unlock(&mutex);
        sem_post(&empty);

        printf("Warehouse: ");
        for (int m = 0; m < warehouseSize; m++)
        {
            printf("%c ", warehouse[m]);
        }
        printf("\n");
    }
    return NULL;
}

int main()
{
    /*initializing thread,mutex,semaphore*/
    pthread_t Far[5],Sho[5];
    pthread_mutex_init(&mutex, NULL);
    sem_init(&empty,0,warehouseSize); //when the warehouse is full thread will wait
    sem_init(&full,0,0); //when the warehouse is empty thread will wait


    int a[5] = {1,2,3,4,5}; //Just used for numbering the Farmer and ShopOwner

    for (int i = 0; i < 5; i++)
    {
        pthread_create(&Far[i], NULL, Farmer, (void *)&a[i]);
        pthread_create(&Sho[i], NULL, ShopOwner, (void *)&a[i]);
    }

    for (int i = 0; i < 5; i++)
    {
        pthread_join(Far[i], NULL);
        pthread_join(Sho[i], NULL);
    }

    //  Closing or destroying mutex and semaphore
    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);

    return 0;
}
