#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
	int p = 0;
	int sum = 0, total = 0;
	vector <int> vec;

	scanf("%d", &p);

	for (int i = 0; i < p; i++) {
		int input = 0;
		scanf("%d", &input);
		vec.push_back(input);
	}
	sort(vec.begin(), vec.end());

	for (int i = 0; i < vec.size(); i++) {
		sum += vec[i];
		total += sum;
	}
	printf("%d", total);
}