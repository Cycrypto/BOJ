#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void) {
	int N, M = 0;
	int arr[100][100];	//�迭 ����
	int max = 0;

	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; i++) {
		int input = 0;
		int j = M-1;

		scanf("%d", &input);
		do {
			
			arr[i][j] = input % 10;
			input /= 10;
			j--;
		} while (input > 0);
	}	//�䱸���׿� �°� �迭�� �Է¹���

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			printf("%3d", arr[i][j]);
		}
		printf("\n");
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M - 2; j++) {

		}
	}
}