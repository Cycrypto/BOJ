#define	_CRT_SECURE_NO_WARNINGS
#define INF 1100000000
#include <iostream>
#include <queue>
#include <vector>

using namespace std;
vector <pair<int, int>>MAP[100000];

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
	int V, E, start;
	cin >> V >> E;	// ÀÔ·Â¹Þ±â
	cin >> start;
	for (int i = 0; i < V; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		MAP[a].push_back(make_pair(b, c));
	}

	vector <int> result = dijkstra(start, V + 1);

	for (int i = 1; i <= V; i++) {
		if (result[i] == INF)
			printf("INF\n");

		else {
			printf("%d\n", result[i]);
		}
	}
}