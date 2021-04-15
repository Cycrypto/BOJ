#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;


vector<int> dp;	//dp 벡터 생성
vector<bool> mal(10, false);	// 고장난 버튼

bool check(int now) {

	string s = to_string(now);	//고장난 채널의 번호가 있는지 확인
	for (int i = 0; i < s.length(); i++) {
		if (mal[s[i] - 48]) {
			return false;
		}

	}

	return true;

}



int main() {

	int n, c;
	cin >> n >> c; //n과 c를 입력받음

	int tmp;

	for (int i = 0; i < c; i++) {
		cin >> tmp;
		mal[tmp] = true;
	}	//고장난 버튼 입력받는 반복문


	string st = to_string(n); // 현재 채널을 문자열로 변환함

	int minimum = abs(n - 100);	//절대값을 씌워 현재 채널과 최솟값을 구함.
	for (int i = 0; i <= 1000000; i++) {

		if (check(i)) {
			int tmp = abs(n - i) + to_string(i).length();
			minimum = min(minimum, tmp);
		}
	}

	cout << minimum << endl;
	return 0;
}