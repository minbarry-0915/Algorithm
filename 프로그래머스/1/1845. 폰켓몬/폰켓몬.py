def solution(nums):
    n = len(nums)
    unique_count = len(set(nums))  # 폰켓몬 종류 수
    return min(unique_count, n // 2)