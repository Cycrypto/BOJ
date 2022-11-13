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
	while (i != 1 && item.key > h->heap[i / 2].key) {//만약 현재 item이 부모노드보다 크다면
		h->heap[i] = h->heap[i / 2];	// 부모노드 인덱스로 이동
		i /= 2;
	}
	h->heap[i] = item;	//적당한 위치에 대입
}

element DelHeap(Heap* h) {
	int parent, child;
	element item, temp;

	item = h->heap[1]; // 루트 노드 값을 반환하기 위해 item에 할당
	temp = h->heap[(h->heap_size)--]; // 마지막 노드를 temp에 할당하고 힙 크기를 하나 감소
	parent = 1;
	child = 2;

	while (child <= h->heap_size) {
		// 현재 노드의 자식 노드 중 더 큰 자식 노드를 찾는다. (루트 노드의 왼쪽 자식 노드(index: 2)부터 비교 시작)
		if ((child < h->heap_size) && ((h->heap[child].key) < h->heap[child + 1].key)) {
			child++;
		}
		// 더 큰 자식 노드보다 마지막 노드가 크면, while문 중지
		if (temp.key >= h->heap[child].key) {
			break;
		}
		// 더 큰 자식 노드보다 마지막 노드가 작으면, 부모 노드와 더 큰 자식 노드를 교환
		h->heap[parent] = h->heap[child];
		// 한 단계 아래로 이동
		parent = child;
		child *= 2;
	}
	// 마지막 노드를 재구성한 위치에 삽입
	h->heap[parent] = temp;
	// 최댓값(루트 노드 값)을 반환
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