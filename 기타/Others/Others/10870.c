#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int fivo(int n) {
	if (n == 0)
		return 0;
	if (n == 1)
		return 1;
	else
		return fivo(n - 1) + fivo(n - 2);
}

int main(void) {
	int input = 0;
	scanf("%d", &input);
	printf("%d", fivo(input));
}