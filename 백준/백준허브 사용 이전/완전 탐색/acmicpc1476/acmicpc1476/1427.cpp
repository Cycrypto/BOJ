#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
	int input = 0;
	scanf("%d", &input);
	vector <int> vec;
	vector <int>::iterator ptr;
	do {
		vec.push_back(input % 10);
		input /= 10;
	} while (input > 0);

	sort(vec.begin(), vec.end());
	reverse(vec.begin(), vec.end());	// 내림차순 정렬

	for (ptr = vec.begin(); ptr != vec.end(); ++ptr)
	{
		printf("%d", *ptr);
	}
}