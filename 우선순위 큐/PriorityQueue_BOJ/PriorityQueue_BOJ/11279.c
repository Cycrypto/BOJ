#define _CRT_SECURE_NO_WARNINGS
#define MAX 100000
#define PARENT(x) x/2

#include <stdio.h>
#include <stdlib.h>

typedef struct{
	long long int data;
}element;

typedef struct {
	int size;
	element heap[MAX];
}Heap;

Heap* create(void) {
	return (Heap*)malloc(sizeof(Heap));
}

void init(Heap* h) {
	h->size = 0;
}

void insert(Heap* h, element e) {
	int i = ++(h->size);	//ÈüÀÇ Å©±â¸¦ ÇÏ³ª ´Ã¸²
	while (i != 1 && e.data < h->heap[i].data) {
		h->heap[i] = h->heap[PARENT(i)];
		i = PARENT(i);
	}
	h->heap[i] = e;
}

element* pop(Heap* h) {

}

int main(void) {

}