#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;


vector<int> dp;	//dp ���� ����
vector<bool> mal(10, false);	// ���峭 ��ư

bool check(int now) {

	string s = to_string(now);	//���峭 ä���� ��ȣ�� �ִ��� Ȯ��
	for (int i = 0; i < s.length(); i++) {
		if (mal[s[i] - 48]) {
			return false;
		}

	}

	return true;

}



int main() {

	int n, c;
	cin >> n >> c; //n�� c�� �Է¹���

	int tmp;

	for (int i = 0; i < c; i++) {
		cin >> tmp;
		mal[tmp] = true;
	}	//���峭 ��ư �Է¹޴� �ݺ���


	string st = to_string(n); // ���� ä���� ���ڿ��� ��ȯ��

	int minimum = abs(n - 100);	//���밪�� ���� ���� ä�ΰ� �ּڰ��� ����.
	for (int i = 0; i <= 1000000; i++) {

		if (check(i)) {
			int tmp = abs(n - i) + to_string(i).length();
			minimum = min(minimum, tmp);
		}
	}

	cout << minimum << endl;
	return 0;
}