#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;
vector <int>graph[26];
bool visited[26];
vector <int> result;

void dfs(int start) {
	queue <int> q;
	visited[start] = true;
	q.push(start);
	while (!q.empty()) {
		int tmp = q.front();
		result.push_back(tmp);
		q.pop();

		for (int i = 0; i < graph[tmp].size(); i++) {
			if (!visited[graph[tmp][i]]) {
				q.push(graph[tmp][i]);
				visited[graph[tmp][i]] = true;
			}
		}
	}
}
int main(void) {
	fill(visited, visited + 26, false);	// 방문을 모두 false 로 초기화
	int tc;
	cin >> tc;
	for (int i = 0; i < tc; i++) {
		for (int j = 0; j < tc; j++) {
			int n;
			scanf("%1d", &n);
			graph[i].push_back(n);
		}
	}
	for (int i = 0; i < tc; i++) {
		for (int j = 0; j < graph[i].size(); j++) {
			printf("%d ", graph[i][j]);
		}
		printf("\n");
	}
}