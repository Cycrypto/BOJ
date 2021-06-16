#define _CRT_SECURE_NO_WARNINGS
#define MAX 101
#include <stdio.h>
#include <stdlib.h>
int MAP[100][100] = { 0 };
int DIST[100][100] = { 0 };
int Queue[MAX * MAX] = { 0 };

void DFS(int x, int y) {
	int front, rear;
	front = rear = 0;
	int pop;

}
int main(void) {
	int N, M;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%1d", &MAP[i][j]);
		}
	}

}