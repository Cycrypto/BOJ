import sys

# N, S = sys.stdin.readline().split(' ')   #input 속도 개선 버전
N,S = map(int,sys.stdin.readline().strip().split())
ar = [int(x) for x in sys.stdin.readline().strip().split()] # 한줄로 입력받아 (띄어쓰기로) 리스트에 저장
size = 1
start,end = 0,1

result = 0

while (size <= N):
    if (sum(ar[start:end]) == S):  #만약 부분합이 입력값과 같은 경우
        result = size
        break
    else:
        if (end >= N - 1):
            size += 1
            start = 0
            end = size

        else:
            start += 1
            end += 1



print(result)


