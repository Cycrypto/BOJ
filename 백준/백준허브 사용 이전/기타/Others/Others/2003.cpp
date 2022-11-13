#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	long long size, sum = 0, ans = 0;
	int fp = 0, lp = 0;
	int result = 0;
	scanf("%lld %lld", &size, &sum);

	long long *A = (long long *)malloc(sizeof(long long) * size);
	for (int i = 0; i < size; i++) {
		long long input = 0;
		scanf("%lld", &input);
		A[i] = input;
	}
	
	while (fp <= lp && lp <= size + 1) {
		if (result >= sum) {
			if (result == sum) {
				ans++;
				result -= A[fp++];
			}
		}

		else {
			if (lp == size + 1)
				break;
			result += A[lp++];
		}
	}
	printf("%d", ans);
}