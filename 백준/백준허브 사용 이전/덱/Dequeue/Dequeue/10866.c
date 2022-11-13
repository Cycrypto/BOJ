#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 100000
typedef int element;
typedef struct {
	element *data;
	int front, rear;
}DequeType;

void error(char* message) {
	fprintf(stderr, "%s/\n", message);
	exit(1);
}

void initDeque(DequeType* q) {
	q->front = q->rear = 0;
	q->data = (DequeType *)malloc(sizeof(element) * MAX_QUEUE_SIZE);
}

int isEmpty(DequeType* q) {
	return (q->front == q->rear);
}

int isFull(DequeType* q) {
	return((q->rear + 1) % MAX_QUEUE_SIZE == q->front);
}

void dequePrint(DequeType* q) {
	printf("DEQUE(front=%d rear=%d)", q->front, q->rear);
	if (!isEmpty(q)) {
		int i = q->front;
		do {
			i = (i + 1) % MAX_QUEUE_SIZE;
			printf("%d | ", q->data[i]);
			if (i == q->rear)
				break;
		} while (i != q->front);
	}
	printf("\n");
}

void addRear(DequeType* q, element item) {
	if (isFull(q)) {
		error("큐가 포화상태입니다.");
	}
	q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
	q->data[q->rear] = item;
}

element deleteRear(DequeType* q) {
	int prev = q->rear;
	if (isEmpty(q)) {
		error("큐가 공백상태입니다.");
	}
	q->rear = (q->rear - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE;
	return q->data[prev];
}

element getRear(DequeType* q) {
	if (isEmpty(q))
		error("큐가 공백상태입니다.");
	return q->data[q->rear];
}
void addFront(DequeType* q, element item) {
	if (isFull(q)) {
		error("큐가 포화상태입니다.");
	}
	q->data[q->front] = item;
	q->front = (q->front - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE;
}

element deleteFront(DequeType* q) {
	int prev = q->rear;
	if (isEmpty(q)) {
		error("큐가 공백상태입니다.");
	}
	q->rear = (q->rear - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE;
	return q->data[prev];
}
element getFront(DequeType* q) {
	if (isEmpty(q)) {
		error("큐가 공백상태입니다.");
	}
	return q->data[(q->front + 1) % MAX_QUEUE_SIZE];
}

int main(void) {
	DequeType queue;
	initDeque(&queue);
	for (int i = 0; i < 3; i++) {
		addFront(&queue, i);
		dequePrint(&queue);
	}
	for (int i = 0; i < 3; i++) {
		deleteRear(&queue);
		dequePrint(&queue);
	}
	return 0;
}