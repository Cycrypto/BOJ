
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int number = 4;
int INF = 100000000;

vector <pair<int, int> >a[7];	// ����, ����� �Ÿ��� ������ pair vector
int d[7];	// ���õ� ���κ��� ����� �������� �Ÿ��� ������ �迭

void dijkstra(int start) {
	d[start] = 0;	// ���õ� ���� ���� �Ÿ��� 0
	priority_queue<pair<int, int>> pq;	//�켱���� ť ����
	pq.push(make_pair(start, 0));

	while (!pq.empty()) {	// �켱���� ť�� ������� �ʴ� ���� �ݺ��� ����
		int current = pq.top().first;	// ���� �湮 ���
		int distance = -pq.top().second;	// ������ �������μ� �� �� ���� ���� ������ ������ ��. (grater<int>)��� �ص� ��,
		pq.pop();	// �� start�� ����� ������ �� ���� ª�� �� �̾Ƴ�.

		if (d[current] < distance)	continue;	// �ִ� �Ÿ��� �ƴ� ��� ��ŵ

		for (int i = 0; i < a[current].size(); i++) {	
			int next = a[current][i].first;
			int nextDistance = distance + a[current][i].second;

			if (nextDistance < d[next]) {
				d[next] = nextDistance;
				pq.push(make_pair(next, -nextDistance));
			}
		}
	}
}

int main(void) {
	for (int i = 1; i <= number; i++) {
		d[i] = INF;
	}

	a[1].push_back(make_pair(2, 1));
	a[1].push_back(make_pair(3, 1));

	a[2].push_back(make_pair(3, 1));
	a[2].push_back(make_pair(4, 1));

	dijkstra(1);
	for (int i = 1; i <= number; i++)
		printf("%d ", d[i]);

}