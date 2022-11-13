#include <cstdio>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int v, e, start;
const int INF = 987654321;
vector<pair<int, int> > adj[20001];
int main() {
	vector<int> dist(20001, INF);
	scanf("%d %d %d", &v, &e, &start);
	for (int i = 0; i < e; ++i) {
		int a, b, c; scanf("%d %d %d", &a, &b, &c);
		adj[a].push_back(make_pair(b, c));
	}
	dist[start] = 0;
	priority_queue<pair<int, int> > pq;
	pq.push(make_pair(0, start));

	while (!pq.empty()) {
		int cost = -pq.top().first;
		int cur = pq.top().second;
		pq.pop();

		if (dist[cur] < cost) continue;

		for (auto& there : adj[cur]) {
			int next = there.first;
			int nextDist = cost + there.second;
			if (dist[next] > nextDist) {
				dist[next] = nextDist;
				pq.push(make_pair(-nextDist, next));
			}
		}
	}

	for (int i = 1; i <= v; ++i) {
		if (dist[i] == INF) puts("INF");
		else printf("%d\n", dist[i]);
	}
}