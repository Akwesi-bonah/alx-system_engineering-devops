#include <stdlib.h>
#include<stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - inifinate loop function
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Program that create a zombi process
 * Return: 0
 */

int main(void)
{
	int i;
	pid_t Z_PID;

	for (i = 0; i < 5; i++)
	{
		Z_PID = fork();

		if (Z_PID > 0)
		{
			printf("Zombie process created, PID: %i\n", Z_PID);
		}
		else
			exit(0);
	}

	infinite_while();
	return (0);
}
