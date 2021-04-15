#define	_CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(void) {
	vector <int> data(8);	//내 입력값
	vector <int> my_data(8); // 1~8까지 넣은 데이터

	for (int i = 0; i < 8; i++) {
		int temp = 0;
		scanf("%d", &temp);
		data.push_back(temp);
	}

	//sort(data.begin(), data.end());


	for (int i = 0; i < 8; i++) {
		my_data[i] = i + 1;
	}

	for (int i = 0; i < 8; i++) {
		if (my_data[i] == data[i])
			continue;
	}
}