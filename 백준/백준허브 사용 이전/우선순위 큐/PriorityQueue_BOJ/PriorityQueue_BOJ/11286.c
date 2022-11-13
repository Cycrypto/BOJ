#define _CRT_SECURE_NO_WARNINGS
#define PARENT(x) x/2
#define MAX 100001

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct _key {
	int key;
}KEY;
typedef struct _heap {
	KEY data[MAX];
	int size;
}Heap;

Heap* create(void) {
	return (Heap *)malloc(sizeof(Heap));
}

void init(Heap* h) {
	h->size = 0;
}

void AbsHeap(Heap* h, KEY item) {
	int i = ++(h->size);
	while (i != 1 && (abs(item.key) < abs(h->data[PARENT(i)].key))) {
		h->data[i] = h->data[PARENT(i)];
		i = PARENT(i);
	}

	h->data[i] = item;

}
KEY AbsHeapPop(Heap* h) {
	int parent = 1, child = 2;
	KEY temp, item;

	item = h->data[1];
	temp = h->data[(h->size)--];

	while (child <= h->size) {
		if ((child < h->size) && ((abs(h->data[child].key)) > abs(h->data[child + 1].key))) {
			child++;
		}

		if (abs(temp.key) < abs(h->data[child].key)) {
			break;
		}

		h->data[parent] = h->data[child];
		parent = child;
		child *= 2;
	}
	h->data[parent] = temp;

	return item;
}
int main(void) {
	int iter = 0, size = 0;
	Heap* h = NULL;
	h = create();
	init(h);

	scanf("%d", &iter);
	for (int i = 0; i < iter; i++) {
		KEY k;
		scanf("%d", &k.key);
		if (k.key != 0) {
			AbsHeap(h, k);
			size++;
		}
		else {
			if (h->size != 0)
				printf(">>%d\n", AbsHeapPop(h).key);
			else
				printf(">>%d\n", 0);
		}
	}
	//while (size--) {
	//	printf("size : %d\n", h->size);
	//	if (h->size != 0)
	//		printf("%d\n", AbsHeapPop(h).key);
	//	else
	//		printf("%d\n", 0);
	//}
}