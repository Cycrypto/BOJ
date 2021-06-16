#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int Graph[1001][1001] = { 0 };
int DFSvisit[1001] = { 0 };
int BFSvisit[1001] = { 0 };
int queue[1001];

void DFS(int v, int n) {	//v는 정점 n은 간선
	DFSvisit[v] = 1;
	printf("%d ", v);

	for (int i = 0; i <= n; i++) {
		if (Graph[v][i] == 1 && DFSvisit[i] == 0)
			DFS(i, n);
	}
}

void BFS(int v, int n) {
	int front = 0, rear = 0;
	int pop;
	printf("%d ", v);
	queue[0] = v;
	rear++;
	BFSvisit[v] = 1;

	while (front < rear) {
		pop = queue[front];
		front++;

		for (int i = 0; i <= n; i++) {
			if (Graph[pop][i] == 1 && BFSvisit[i] == 0) {
				printf("%d ", i);
				queue[rear] = i;
				rear++;
				BFSvisit[i] = 1;
			}
		}
	}
}

int main(void) {
	int N, M, S;
	int x, y;
	scanf("%d %d %d", &N, &M, &S);
	for (int i = 0; i < M; i++) {
		scanf("%d %d", &x, &y);
		Graph[x][y] = 1;
		Graph[y][x] = 1;
	}

	DFS(S, N);
	printf("\n");
	BFS(S, N);
}