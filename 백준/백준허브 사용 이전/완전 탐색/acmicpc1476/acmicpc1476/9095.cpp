#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

using namespace std;

int cnt = 0;

void add(int sum, int goal) {
	if (sum > goal) return;
	else if (sum == goal) {
		cnt++;
		return;
	}
	else {
		for (int i = 1; i <= 3; i++) {
			add(sum + i, goal);
		}
	}
}

int main() {

	int t, n;

	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		cnt = 0;
		scanf("%d", &n);
		add(0, n);
		printf("%d\n", cnt);
	}

	return 0;
}