#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int input = 0, fact = 1;
	scanf("%d", &input);
	while (input > 0) {
		fact *= input;
		input--;
	}
	printf("%d", fact);
}