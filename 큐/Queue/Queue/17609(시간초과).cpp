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
			deq.push_back(*(ch + j));	//	덱의 인덱스에 각각 하나씩 문자를 집어넣음 (배열처럼 사용)
		}

		while (!deq.empty()) {
			if (deq.front() == deq.back()) {
				deq.pop_front(); deq.pop_back();	// 덱의 앞 뒤가 같다면 pop함
			}
			else {
				if (*(&deq.front() + 1) == deq.back()) {
					deq.pop_front();	// front를 삭제시켰을 때 회문이라면
					result = SEMI_PALINDROME;
				}
				else if (*(&deq.back() - 1) == deq.front()) {
					deq.pop_back();	//back을 삭제시켰을 때 회문이라면
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