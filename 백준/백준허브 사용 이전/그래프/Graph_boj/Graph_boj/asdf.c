#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void main(void)
{
	int n, a, b, c = 0, cnt = 0;
	int s = 0;
	printf("2 �̻� ���� �Է�:   ");
	scanf("%d", &n);
	printf("%d ������ �Ҽ� : ", n);
	for (a = 1; a <= n; a++) {

		for (b = 1; b <= a; b++) {
			if (a % b == 0) {
				cnt++;
			}
		}
		if (cnt == 2) {
			printf("%5d", a);
			s+= a;
		}
		cnt = 0;

	}
	printf("\n�� : %d", s);
}