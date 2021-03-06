
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stack>
#include <vector>
using namespace std;
int main() {
	int n;
	vector<int> v;
	stack<int> s;
	vector<char> d;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		int k;
		scanf("%d", &k);
		v.push_back(k);
	}
	vector<int>::iterator it;
	it = v.begin();
	for (int i = 1; i <= n; ++i) {
		s.push(i);
		d.push_back('+');
		while (!s.empty()) {
			if (*it != s.top()) break;
			else {
				s.pop();
				d.push_back('-');
				++it;
			}
		}
	}
	if (s.empty()) {
		for (int i = 0; i < d.size(); ++i)
			printf("%c\n", d[i]);
	}

	else
		printf("NO");
}