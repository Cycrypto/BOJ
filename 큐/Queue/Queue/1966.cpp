#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>

using namespace std;

int main(void) {

	int iter = 0;
	scanf("%d", &iter);
	for (int it = 0; it < iter; it++) {
		queue <pair <int, int>> q;
		priority_queue<int, vector<int>> pq;

		int cnt = 0, pos = 0, pri = 0;
		int iOutputCount = 0;
		scanf("%d %d", &cnt, &pos);	// 문서의 개수, 위치

		for (int j = 0; j < cnt; j++) {
			int input = 0;
			scanf("%d", &input);
			q.push(make_pair(j, input));	//프린트 대기열
			pq.push(input);	//우선순위 큐에 값 전달
		}
		
		while (!q.empty())
		{
			int currIndex = q.front().first;
			int currValue = q.front().second;

			q.pop();

			if (pq.top() == currValue)
			{
				pq.pop();
				iOutputCount++;

				if (currIndex == pos)
				{
					printf("%d\n", iOutputCount);
					break;
				}
			}
			else
			{
				q.push({ currIndex ,currValue });
			}
		}
	}// 테스트 케이스 개수
}