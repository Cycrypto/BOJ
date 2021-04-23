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
		scanf("%d %d", &cnt, &pos);	// ������ ����, ��ġ

		for (int j = 0; j < cnt; j++) {
			int input = 0;
			scanf("%d", &input);
			q.push(make_pair(j, input));	//����Ʈ ��⿭
			pq.push(input);	//�켱���� ť�� �� ����
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
	}// �׽�Ʈ ���̽� ����
}