#define _CRT_SECURE_NO_WARNINGS
#define MAX 2000001

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef int element;
typedef struct {
	int front, rear;
	int *data;
}QueueType;

void init(QueueType* q) {
	q->front = -1;
	q->rear = -1;
	q->data = (int*)malloc(MAX);
}

bool is_empty(QueueType* q) {
	return q->front == q->rear;
}

void push(QueueType* q, element item) {
	q->data[++(q->rear)] = item;
}

element pop(QueueType* q) {
	if (is_empty(q))
		return -1;
	return q->data[++(q->front)];
}

element qsize(QueueType* q) {
	return q->rear - q->front;
}

element front(QueueType* q) {
	return q->front + 2;
}

element back(QueueType* q) {
	return q->rear + 1;
}
int main(void) {
	QueueType q;
	init(&q);
	int iter = 0;
	char* string = (char *)malloc(sizeof(char) * 10);
	scanf("%d", &iter);
	for (int i = 0; i < iter; i++) {
		int item = 0;
		scanf("%s", string);
		
		if (!strcmp(string, "push")) {
			scanf("%d", &item);
			push(&q, item);
		}
		else if (!strcmp(string, "pop")) {
			printf("%d\n", pop(&q));
		}
		else if (!strcmp(string, "size")) {
			printf("%d\n", qsize(&q));
		}
		else if (!strcmp(string, "empty")) {
			printf("%d\n", is_empty(&q));
		}
		else if (!strcmp(string, "front")) {
			printf("%d\n", front(&q));
		}
		else {
			printf("%d\n", back(&q));
		}
	}
	free(string);
}