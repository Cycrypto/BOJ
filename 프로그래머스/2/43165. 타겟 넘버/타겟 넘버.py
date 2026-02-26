def solution(numbers, target):
    def dfs(n, s):
        if n == len(numbers):
            return 1 if s == target else 0
        
        return dfs(n+1, s + numbers[n]) + dfs(n+1, s - numbers[n])
    return dfs(0, 0)