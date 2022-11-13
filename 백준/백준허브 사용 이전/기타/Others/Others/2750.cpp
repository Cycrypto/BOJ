#define	_CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(void) {
	int input = 0;
	vector <int> data;
	scanf("%d", &input);
	for (int i = 0; i < input; i++) {
		int temp = 0;
		scanf("%d", &temp);
		data.push_back(temp);
	}
	sort(data.begin(), data.end());


	for (int i = 0; i < input; i++) {
		printf("%d\n", data[i]);
	}
}