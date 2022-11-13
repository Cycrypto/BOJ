#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>

using namespace std;

int main(void) {
	queue <int> q;
	int num = 0;
	scanf("%d", &num);

	for (int i = 1; i <= num; i++) {
		q.push(i);
	}

	while (q.size() > 1) {
		int temp = 0;
		q.pop();
		temp = q.front();
		q.pop();
		q.push(temp);
	}

	printf("%d\n", q.front());
}