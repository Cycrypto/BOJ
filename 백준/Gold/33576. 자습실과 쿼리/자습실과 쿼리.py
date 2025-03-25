import sys
input = sys.stdin.readline

# 입력 받기: 구역의 개수 N, 벽의 개수 M, 학생의 수 Q
N, M, Q = map(int, input().split())

# 1번부터 N번 구역에 대해 벽 내구도를 저장 (벽이 없는 구역은 0)
wall = [0] * (N + 1)
for _ in range(M):
    pos, dur = map(int, input().split())
    wall[pos] = dur

# 누적합(prefix) 배열: prefix[i]는 1번부터 i번까지 벽 내구도의 총합
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + wall[i]

# 투포인터: 이미 파괴된 벽의 범위를 관리하는 포인터들
# leftClear: 좌측(출구 1 쪽)에서 파괴된 벽의 가장 오른쪽 인덱스 (초기 0)
# rightClear: 우측(출구 N 쪽)에서 파괴된 벽의 가장 왼쪽 인덱스 (초기 N+1)
leftClear = 0
rightClear = N + 1

results = []
for _ in range(Q):
    p = int(input())
    # 이미 출구(1 또는 N)에 있으면 추가 비용 0
    if p == 1 or p == N:
        results.append("0")
        continue

    # 남아있는 좌측 벽의 내구도 합 계산: (leftClear+1)번부터 (p-1)번까지
    if p - 1 > leftClear:
        cost_left = prefix[p - 1] - prefix[leftClear]
    else:
        cost_left = 0

    # 남아있는 우측 벽의 내구도 합 계산: (p+1)번부터 (rightClear-1)번까지
    if p + 1 < rightClear:
        cost_right = prefix[rightClear - 1] - prefix[p]
    else:
        cost_right = 0

    # 먼저 망치질 횟수가 적은 쪽을 선택
    if cost_left < cost_right:
        chosen_cost = cost_left
        # 좌측 탈출 시, 1번부터 p-1번 구역의 벽이 모두 파괴됨 → leftClear를 p-1로 업데이트
        leftClear = max(leftClear, p - 1)
    elif cost_left > cost_right:
        chosen_cost = cost_right
        # 우측 탈출 시, p+1번부터 N번 구역의 벽이 모두 파괴됨 → rightClear를 p+1로 업데이트
        rightClear = min(rightClear, p + 1)
    else:
        # 망치질 횟수가 같으면, 이동 거리를 비교 (좌측: p-1, 우측: N-p)
        if (p - 1) <= (N - p):
            chosen_cost = cost_left
            leftClear = max(leftClear, p - 1)
        else:
            chosen_cost = cost_right
            rightClear = min(rightClear, p + 1)
    results.append(str(chosen_cost))

print("\n".join(results))