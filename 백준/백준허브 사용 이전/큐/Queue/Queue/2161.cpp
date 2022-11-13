#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>

using namespace std;
int main(void) {
	queue <int> q;
	int iter = 0;
	scanf("%d", &iter);
	for (int i = 0; i < iter; i++) {
		q.push(i + 1);
	}
	while (!q.empty()) {
		printf("%d ", q.front());
		q.pop();
		if (q.empty())
			break;
		int temp = q.front();
		q.pop();
		q.push(temp);
	}
}