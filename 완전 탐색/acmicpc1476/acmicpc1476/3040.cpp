#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main(void) {
	vector <int>num(9);
	for (int i = 0; i < num.size(); i++) {
		int input = 0;
		scanf("%d", &input);
		num[i] = input;
	}


	for (int i = 0; i < num.size() - 1; i++) {
		for (int j = 1; j < num.size(); j++) {
			if (accumulate(num.begin(), num.end(), 0) - num[i] - num[j] == 100) {
				num[i] = num[j] = -1;
			}
		}
	}

	for (int i = 0; i < num.size(); i++) {
		if (num[i] > 0)
			printf("%d\n", num[i]);
		else
			continue;
	}
}