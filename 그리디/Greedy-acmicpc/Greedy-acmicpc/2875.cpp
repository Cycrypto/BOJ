#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int N, M, K;
	int team = 0;
	scanf("%d %d %d", &N, &M, &K);
	while (N > 0 && M > 0) {
		N -= 2;
		M -= 1;
		team++;
	}
	printf("Team : %d\n****************\n", team);
	while (K > 0) {
		//printf("BEF => N : %d\nM : %d\nK : %d\n\n", N, M, K);
		if (N != 0 && K >= 2) {
			K -= N; N = 0;
		}

		else if (M != 0 && K >= 1) {
			K -= M; M = 0;
		}

		else {
			team--;
			N += 2; M += 1;
		}
		//printf("AFT => N : %d\nM : %d\nK : %d\n\n", N, M, K);
	}
	printf("%d",team);
}