#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
	vector <long> Node;
	vector <long> Dist;

	long input = 0;
	long sum = 0;
	scanf("%d", &input);
	for (int i = 0; i < input - 1; i++) {
		int d = 0;
		scanf("%d", &d);
		Dist.push_back(d);
	}

	for (int j = 0; j < input; j++) {
		int n = 0;
		scanf("%d", &n);
		Node.push_back(n);
	}
	long m = Dist[0] * Node[0];

	for (int k = 0; k < input - 1; k++) {
		m = min(m, Node[k]);
		sum += m * Dist[k];
	}
	printf("%ld", sum);
}