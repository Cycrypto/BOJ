#define _CRT_SECURE_NO_WARNINGS
#define PARENT(x) x/2
#define MAXSIZE 100

#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int data;
}element;

typedef struct {
	element heap[MAXSIZE];
	int size;
}Heap;

Heap* create(void) {
	return (Heap*)malloc(sizeof(Heap));
}

void init(Heap* h) {
	h->size = 0;
}

void insert_up(Heap* h, element item) {
	int i = ++(h->size);
	while (i != 1 && item.data < h->heap[PARENT(i)].data) {
		h->heap[i] = h->heap[PARENT(i)];
		i = PARENT(i);
	}
	h->heap[i] = item;
}

element delete_heap(Heap* h) {

	if (h->size == 0) {
		element e = { 0 };
		return e;
	}

	int parent = 1, child = 2;
	element item, temp;
	item = h->heap[1];
	temp = h->heap[h->size--];

	while (child <= h->size) {
		if ((child < h->heap[child + 1].data) && (h->heap[child].data < h->heap[child + 1].data))
			child++;

		if (temp.data >= h->heap[child].data)
			break;

		h->heap[parent] = h->heap[child];
		parent = child;
		child *= 2;
	}
	h->heap[parent] = temp;
	return item;
}
int* asc(element* h, int size) {
	Heap* space = create();
	element *e = malloc(sizeof(element));
	init(space);
	for (int i = 0; i < size; i++) {
		if (h[i].data == 0) {
			e[i] = delete_heap(space);
			insert_up(space, e[i]);
		}

		else
			insert_up(space, h[i]);
	}
	return h;
}

int main(void) {
	element e[MAXSIZE];
	int iter = 0, cnt = 0;
	int size = sizeof(e) / sizeof(element);
	scanf("%d", &iter);
	for (int i = 0; i < iter; i++) {
		scanf("%d", &e[i]);
		if (e[i].data == 0)
			cnt++;
	}
	element *e2 = asc(e, iter);
	for (int i = 0; i < cnt; i++) {
		printf("%d\n", e2[i].data);
	}
	return 0;
}