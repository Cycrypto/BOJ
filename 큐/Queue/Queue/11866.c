#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
typedef int element;
typedef struct {
	int rear;
	int front;
	int *data;
	int size;
}QueueType;

void init(QueueType* q, int size) {
	q->rear = 0;
	q->front = 0;
	q->size = size;
	q->data = (element*)malloc(sizeof(element) * (q->size));
}

element dequeue(QueueType* q) {
	return q->data[q->front = (q->front + 1) % q->size];
}

void enqueue(QueueType* q, element item) {
	q->data[q->rear = (q->rear + 1) % q->size] = item;
	//printf("[%p] %d %d\n",q, q->front, q->rear);
}

int main(void) {
	QueueType Queue;
	int size, iter;
	scanf("%d %d", &size, &iter);
	init(&Queue, size);
	for (int i = 1; i <= size; i++) {
		enqueue(&Queue, i);
	}

	printf("<");
	do {
		for (int i = 1; i < iter; i++) {
			int temp = dequeue(&Queue);
			enqueue(&Queue, temp);
		}
		printf("%d", dequeue(&Queue));
		if (Queue.front != Queue.rear)
			printf(", ");

	} while (Queue.front != Queue.rear);
	printf(">");
}