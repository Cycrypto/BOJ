#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int N = 0, M = 0;
	int res = 0, tmp = 0;
	scanf("%d %d", &N, &M);
	vector <int> gugu(M+1);

	for (int i = 1; i <= M; i++) {
		res = N * i;
		int result = 0;
		while (res > 0) {
			result *= 10;
			result += (res % 10);
			res /= 10;
		}
		gugu[i] = result;

	}
	printf("%d", *max_element(gugu.begin(), gugu.end()));
}