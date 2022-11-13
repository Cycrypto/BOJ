#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	int input = 0;
	int max = 0;
	vector <int> vec;
	scanf("%d", &input);
	for (int i = 0; i < input; i++) {
		int N = 0;
		scanf("%d", &N);
		vec.push_back(N);
	}
	sort(vec.begin(), vec.end(), greater<int>());

	for (int i = 0; i < input; i++) {
		if (max < vec[i] * (i + 1))
			max = vec[i] * (i + 1);
	}
	printf("%d", max);
}