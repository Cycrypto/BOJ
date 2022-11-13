#include <iostream>
using namespace std;

int a[41];
int fibonacci(int n) {
	if (n <= 0) {
		a[0] = 0;
		return 0;
	}
	else if (n == 1) {
		a[1] = 1;
		return 1;
	}
	if (a[n] != 0) return a[n];
	else return a[n] = fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		if (n == 0) {
			printf("1 0\n");
		}
		else if (n == 1) {
			printf("0 1\n");
		}
		else {
			fibonacci(n);
			printf("%d %d\n", a[n - 1], a[n]);
		}
	}
	return 0;
}