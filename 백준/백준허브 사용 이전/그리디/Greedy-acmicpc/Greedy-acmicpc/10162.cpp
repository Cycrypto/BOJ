#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
using namespace std;
int main(void) {
	int cA = 0, cB = 0, cC = 0;
	int time = 0, flag = 0;
	scanf ("%d", &time);

	while (time != 0) {
		if (time >= 300) {
			time -= 300;
			cA++;
		}
		
		else if (time >= 60) {
			time -= 60;
			cB++;
		}
		
		else if (time >= 10) {
			time -= 10;
			cC++;
		}

		else {
			flag = 1;
			break;
		}
	}
	if (flag) {
		printf("-1");
	}
	else {
		printf("%d %d %d", cA, cB, cC);
	}
}