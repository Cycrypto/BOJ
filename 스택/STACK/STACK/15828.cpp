#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>

using namespace std;
int main(void) {
	queue <int> q;
	int input = 0;
	int buffer = 0;
	scanf("%d", &buffer);
	while (true) {
		scanf("%d", &input);
		if (input == -1)
			break;

		if (input == 0)
			q.pop();

		else {
			if (q.size() <= buffer)
				q.push(input);
		}
	}
	
	if (!q.empty()) {
		while (!q.empty()) {
			printf("%d ", q.front());
			q.pop();
		}
	}
	else {
		printf("empty");
	}
}