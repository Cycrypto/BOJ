#define _CRT_SECURE_NO_WARNINGS
#define MAX_VERTICS 1001	//최대 정점의 개수
#define MAX_QUEUE_SIZE 10001
#define TRUE 1	
#define FALSE 0

#include <stdio.h>
#include <stdlib.h>

int visited[MAX_VERTICS];
int visited2[MAX_VERTICS];


typedef int element;
typedef struct { // 큐 타입
	element  queue[MAX_QUEUE_SIZE];
	int  front, rear;
} QueueType;

typedef struct GraphNode {
	int vertex; //정점을 나타내는 데이터	== 정점 번호
	struct GraphNode* link;	// 다음 정점을 나타내는 링크
}GraphNode;

typedef struct GraphType {
	int n;	//그래프 정점의 개수
	GraphNode* adj_list[MAX_VERTICS];// 그래프 정점에 대한 헤드 노드
	int adj_mat[MAX_VERTICS][MAX_VERTICS];
}GraphType;

void error(char* message)
{
	fprintf(stderr, "%s\n", message);
	exit(1);
}

// 공백 상태 검출 함수
int is_empty(QueueType* q)
{
	return (q->front == q->rear);
}

// 포화 상태 검출 함수
int is_full(QueueType* q)
{
	return ((q->rear + 1) % MAX_QUEUE_SIZE == q->front);
}

// 공백 상태 검출 함수
void queue_init(QueueType* q)
{
	q->front = q->rear = 0;
}

// 삽입 함수
void enqueue(QueueType* q, element item)
{
	if (is_full(q))
		error("큐가 포화상태입니다");
	q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
	q->queue[q->rear] = item;
}

// 삭제 함수
element dequeue(QueueType* q)
{
	if (is_empty(q))
		error("큐가 공백상태입니다");
	q->front = (q->front + 1) % MAX_QUEUE_SIZE;
	return q->queue[q->front];
}

void init(GraphType* g) {
	int v, r, c;
	g->n = 0;	//그래프 정점의 개수를 0으로 초기화
	for (v = 0; v < MAX_VERTICS; v++) {
		g->adj_list[v] = NULL;
	}

	for (r = 0; r < MAX_VERTICS; r++)
		for (c = 0; c < MAX_VERTICS; c++)
			g->adj_mat[r][c] = 0;
}

void insert_vertex(GraphType* g, int v) {
	if (((g->n) + 1) > MAX_VERTICS) {
		fprintf(stderr, "OverFlow\n");
		return;
	}
	//g->adj_list[++(g->n)] = v;
	g->n++;
}

void insert_edge(GraphType* g, int u, int v) {
	GraphNode* node;
	if (u >= g->n || v >= g->n) {
		fprintf(stderr, "그래프: 정점 번호 오류\n");
		return;
		//정점 u 또는 v의 번호가 그래프의 정점 개수보다 크다면 오류 문구를 프린트합니다.
	}

	g->adj_mat[u][v] = 1;
	g->adj_mat[v][u] = 1;

	node = (GraphNode*)malloc(sizeof(GraphNode));
	node->vertex = v;
	node->link = g->adj_list[u];
	g->adj_list[u] = node;

}

void dfs_list(GraphType* g, int v) {
	GraphNode* w;
	visited[v] = TRUE;	//방문한 것을 True로 표시
	printf("%d ", v);	// 해당 노드 출력
	for (w = g->adj_list[v]; w; w = w->link) {
		if (!visited[w->vertex])
			dfs_list(g, w->vertex);
	}
}

void bfs_mat(GraphType* g, int v) {
	int w;
	QueueType q;
	queue_init(&q);
	visited2[v] = TRUE;

	printf("%d ", v);
	enqueue(&q, v);

	while (!is_empty(&q)){
		v = dequeue(&q);

		for (w = 0; w < g->n; w++) {
			if (g->adj_mat[v][w] && !visited2[w]) {
				visited2[w] = TRUE;
				printf("%d ", w);
				enqueue(&q, w);
			}
		}
	}
}

int main(void) {
	int N, M, S;
	scanf("%d %d %d", &N, &M, &S);

	GraphType* g;
	g = (GraphType*)malloc(sizeof(GraphType));
	init(g);

	for (int i = 1; i <= N + 1; i++)
		insert_vertex(g, i);
	for (int j = 0; j < M; j++) {
		int p, q;
		scanf("%d %d", &p, &q);
		insert_edge(g, p, q);
	}
	dfs_list(g, S);
	printf("\n");
	bfs_mat(g, S);
}