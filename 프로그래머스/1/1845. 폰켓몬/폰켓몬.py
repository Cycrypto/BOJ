def solution(nums):
    num_set = set(nums)
    return min(len(num_set), len(nums) // 2)
