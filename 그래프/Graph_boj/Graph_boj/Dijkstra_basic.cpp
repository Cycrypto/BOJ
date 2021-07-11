
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int number = 4;
int INF = 100000000;

vector <pair<int, int> >a[7];	// 노드와, 연결된 거리를 저장할 pair vector
int d[7];	// 선택된 노드로부터 연결된 노드까지의 거리를 저장할 배열

void dijkstra(int start) {
	d[start] = 0;	// 선택된 노드로 가는 거리는 0
	priority_queue<pair<int, int>> pq;	//우선순위 큐 생성
	pq.push(make_pair(start, 0));

	while (!pq.empty()) {	// 우선순위 큐가 비어있지 않는 동안 반복문 실행
		int current = pq.top().first;	// 현재 방문 노드
		int distance = -pq.top().second;	// 음수를 넣음으로서 뺄 때 가장 작은 수부터 빼도록 함. (grater<int>)사용 해도 됨,
		pq.pop();	// 즉 start에 연결된 간선들 중 가장 짧은 걸 뽑아냄.

		if (d[current] < distance)	continue;	// 최단 거리가 아닌 경우 스킵

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