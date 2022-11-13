#define _CRT_SECURE_NO_WARNINGS
#define INF 987654321
#define MAX 100000

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

vector <pair<int, int>> Computer[MAX];

vector <int> dijkstra(int start, int v) {
	vector <int> d(v, INF);
	priority_queue<pair<int, int>> pq;
	d[start] = 0;
	pq.push(make_pair(0, start));

	while (!pq.empty()) {
		int current = pq.top().second;
		int distance =  -pq.top().first;
		pq.pop();
		if (d[current] < distance)	continue;
		for (int i = 0; i < Computer[current].size(); i++) {
			int next = Computer[current][i].second;
			int nextDistance = distance + Computer[current][i].first;

			if (d[next] > nextDistance) {
				d[next] = nextDistance;
				pq.push(make_pair(-nextDistance, next));
			}
		}
	}
	return d;
}

int main(void) {
	int tc;
	int a, d, c;
	cin >> tc;

	for (int j = 0; j < tc; j++) {
		cin >> a >> d >> c;
		for (int i = 0; i < d; i++) {
			int a, b, s;
			cin >> a >> b >> s;
			Computer[b].push_back(make_pair(s, a));
		}
		vector <int> result = dijkstra(c, a+1);
		int infect = 0, cnt = 0;
		for (int k = 1; k < result.size(); k++) {
			if (result[k] != INF) {
				infect++;
				if (result[k] > cnt)	cnt = result[k];
			}
		}
		cout << infect << " " << cnt << endl;
	}
	return 0;
}