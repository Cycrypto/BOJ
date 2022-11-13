#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main(void) {
	int dial[] = {3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10};
	char input[20];
	int result = 0;

	scanf("%s", input);

	
	for (int i = 0; i < strlen(input); i++) {
		result += dial[input[i]-65];
	}

	printf("%d", result);
}