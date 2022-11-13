#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main(void) {
	stack <double> Stack;
	vector <int> vec;
	int val = 0;
	string ch;
	scanf("%d", &val);
	cin >> ch;
	for (int i = 0; i < val; i++) {
		int k = 0;
		scanf("%d", &k);
		vec.push_back(k);
	}

	double opr1, opr2;
	for (int iter = 0; iter < ch.length(); iter++) {
		if (ch[iter] >= 'A' && ch[iter] <= 'Z')
			Stack.push(vec[ch[iter] - 'A']);
		else {
			opr1 = Stack.top();	Stack.pop();
			opr2 = Stack.top();	Stack.pop();

			switch (ch[iter]) {
			case '+':
				Stack.push(opr2 + opr1);
				break;
			case '-':
				Stack.push(opr2 - opr1);
				break;
			case '*':
				Stack.push(opr2 * opr1);
				break;
			case '/':
				Stack.push(opr2 / opr1);
				break;
			}
		}
	}
	printf("%.2lf", Stack.top());
}