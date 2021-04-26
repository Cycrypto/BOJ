#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>
#include <deque>
#include <vector>

using namespace std;
enum {
	PALINDROME,
	SEMI_PALINDROME,
	NOT_PALINDROME
};

int main(void) {

	int iter = 0;
	scanf("%d", &iter);

	for (int i = 0; i < iter; i++) {
		deque <char> deq;
		int result = PALINDROME;
		char* ch = (char *)malloc(sizeof(char) * 100000);
		scanf("%s", ch);

		for (int j = 0; j < strlen(ch); j++) {
			deq.push_back(*(ch + j));	//	���� �ε����� ���� �ϳ��� ���ڸ� ������� (�迭ó�� ���)
		}

		while (!deq.empty()) {
			if (deq.front() == deq.back()) {
				deq.pop_front(); deq.pop_back();	// ���� �� �ڰ� ���ٸ� pop��
			}
			else {
				if (*(&deq.front() + 1) == deq.back()) {
					deq.pop_front();	// front�� ���������� �� ȸ���̶��
					result = SEMI_PALINDROME;
				}
				else if (*(&deq.back() - 1) == deq.front()) {
					deq.pop_back();	//back�� ���������� �� ȸ���̶��
					result = SEMI_PALINDROME;
				}
				else {
					result = NOT_PALINDROME;
					break;
				}
			}
		}
		printf("%d\n", result);
	}

}