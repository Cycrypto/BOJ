#define _CRT_SECURE_NO_WARNINGS
#define INF 1100000000
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector <pair<int, int>> MAP[100000];

vector<int> dijkstra(int start, int cnt) {
	vector<int> d(cnt, INF);
	d[start] = 0;
	priority_queue<pair<int, int>> pq;
	pq.push(make_pair(start, 0));

	while (!pq.empty()) {
		int current = pq.top().first;
		int distance = -pq.top().second;
		pq.pop();	// °¡Àå ÂªÀº °Å¸® »Ì¾Æ³¿

		if (d[current] < distance)	continue;
		for (int i = 0; i < MAP[current].size(); i++) {
			int next = MAP[current][i].first;
			int nextDistance = distance + MAP[current][i].second;

			if (nextDistance < d[next]) {
				d[next] = nextDistance;
				pq.push(make_pair(next, -nextDistance));
			}
		}
	}
	return d;
}

int main(void) {
	int N, M;
	int start, end;

	scanf("%d\n%d", &N, &M);

	for (int i = 0; i < M; i++) {
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		MAP[a].push_back(make_pair(b, c));
	}	// Graph »ý¼º

	scanf("%d %d", &start, &end);
	vector<int> result = dijkstra(start, N+1);
	printf("%d", result[end]);
}