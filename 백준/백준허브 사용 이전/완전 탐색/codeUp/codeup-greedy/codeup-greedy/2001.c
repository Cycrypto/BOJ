#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int arr1[3] = { 0, };
	int arr2[2] = { 0, };
	int min =99999999999;

	for (int i = 0; i < 3; i++) {
		scanf("%d", &arr1[i]);
	}

	for (int i = 0; i < 2; i++) {
		scanf("%d", &arr2[i]);
	}
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 2; j++) {
			int sum = arr1[i] + arr2[j];
			if (sum < min)
				min = sum;
		}
	}
	printf("%.1lf", min + (min * 0.1));
}