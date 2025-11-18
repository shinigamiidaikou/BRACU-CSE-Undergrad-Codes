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

	struct message msg_to_rcv;

	int rcv = msgrcv(msg_id, (void *)&msg_to_rcv, 200, -5, IPC_NOWAIT);

	if (rcv < 0)
	{
		printf("Error\n");
		return 0;
	}

	printf("Data Type: %ld\n", msg_to_rcv.type);
	printf("Data received: %s\n", msg_to_rcv.txt);

	rcv = msgrcv(msg_id, (void *)&msg_to_rcv, 200, -7, IPC_NOWAIT);

	if (rcv < 0)
	{
		printf("Error\n");
		return 0;
	}

	printf("Data Type: %ld\n", msg_to_rcv.type);
	printf("Data received: %s\n", msg_to_rcv.txt);

	msgctl(msg_id, IPC_RMID, 0);
	return 0;
}
