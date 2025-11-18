#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <string.h>

struct message
{
	long int type;
	char txt[200];
};

int main()
{
	int msg_id;
	msg_id = msgget((key_t)12, 0666 | IPC_CREAT);

	if (msg_id == -1)
	{
		printf("Msg ID Error!\n");
	}

	struct message msg_to_send;

	msg_to_send.type = 6;
	strcpy(msg_to_send.txt, "hello");

	int snt = msgsnd(msg_id, (void *)&msg_to_send, sizeof(msg_to_send.txt), IPC_NOWAIT);

	if (snt < 0)
	{
		printf("Error\n");
		return 0;
	}
	printf("Data Sent: %s\n", msg_to_send.txt);

	msg_to_send.type = 4;
	strcpy(msg_to_send.txt, "hola");

	snt = msgsnd(msg_id, (void *)&msg_to_send, sizeof(msg_to_send.txt), IPC_NOWAIT);

	if (snt < 0)
	{
		printf("Error\n");
		return 0;
	}
	printf("Data Sent: %s\n", msg_to_send.txt);

	return 0;
}
