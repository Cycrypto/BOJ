#include <stdio.h>
#include <ctype.h>
int main(void) {
	char* arr = "hello";
	for (int i = 0; i < strlen(arr); i++) {
		printf("%c", toupper(*(arr + i)));
	}
}