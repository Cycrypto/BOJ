#define _CRT_SECURE_NO_WARNINGS

#define EARTH_MAX 15
#define SUN_MAX 28
#define MOON_MAX 19
#include <iostream>
#include <algorithm>
using namespace std;
int main(void) {
	int E, S, M = 0;
	int i = 1, j = 1, k = 1;
	int year = 1;
	scanf("%d %d %d", &E, &S, &M);
	while (i != E || j != S || k != M) {
		//printf("%d %d %d\n", i, j, k);
		i++, j++, k++;
		if (i > EARTH_MAX)
			i = 1;
		if (j > SUN_MAX)
			j = 1;
		if (k > MOON_MAX)
			k = 1;
		year++;

	}
	printf("%d", year);
}