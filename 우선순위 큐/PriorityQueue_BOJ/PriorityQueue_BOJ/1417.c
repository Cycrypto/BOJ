#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct _key {
	int no;
	int key;
}element;

typedef struct _heap {
	element heap[1001];
	int heap_size;
}Heap;

Heap* create(void) {
	return (Heap*)malloc(sizeof(Heap));
}

void init(Heap* h) {
	h->heap_size = 0;
}

void MaxHeap(Heap* h, element item) {
	int i = ++(h->heap_size);
	while (i != 1 && item.key > h->heap[i / 2].key) {//���� ���� item�� �θ��庸�� ũ�ٸ�
		h->heap[i] = h->heap[i / 2];	// �θ��� �ε����� �̵�
		i /= 2;
	}
	h->heap[i] = item;	//������ ��ġ�� ����
}

element DelHeap(Heap* h) {
	int parent, child;
	element item, temp;

	item = h->heap[1]; // ��Ʈ ��� ���� ��ȯ�ϱ� ���� item�� �Ҵ�
	temp = h->heap[(h->heap_size)--]; // ������ ��带 temp�� �Ҵ��ϰ� �� ũ�⸦ �ϳ� ����
	parent = 1;
	child = 2;

	while (child <= h->heap_size) {
		// ���� ����� �ڽ� ��� �� �� ū �ڽ� ��带 ã�´�. (��Ʈ ����� ���� �ڽ� ���(index: 2)���� �� ����)
		if ((child < h->heap_size) && ((h->heap[child].key) < h->heap[child + 1].key)) {
			child++;
		}
		// �� ū �ڽ� ��庸�� ������ ��尡 ũ��, while�� ����
		if (temp.key >= h->heap[child].key) {
			break;
		}
		// �� ū �ڽ� ��庸�� ������ ��尡 ������, �θ� ���� �� ū �ڽ� ��带 ��ȯ
		h->heap[parent] = h->heap[child];
		// �� �ܰ� �Ʒ��� �̵�
		parent = child;
		child *= 2;
	}
	// ������ ��带 �籸���� ��ġ�� ����
	h->heap[parent] = temp;
	// �ִ�(��Ʈ ��� ��)�� ��ȯ
	return item;
}

int main(void) {
	int iter = 0;
	int comp = 0, result = 0;
	Heap* heap;
	heap = create();
	init(heap);
	scanf("%d", &iter);
	scanf("%d", &comp);

	for (int i = 0; i < iter - 1; i++) {
		element e;
		e.no = i + 1;
		scanf("%d", &e.key);
		MaxHeap(heap, e);
	}

	while (heap->heap_size != 0) {
		element e2 = DelHeap(heap);
		if (comp > e2.key --)
			break;

		MaxHeap(heap, e2);
		comp++;
		result++;
	}
	printf("%d", result);
}