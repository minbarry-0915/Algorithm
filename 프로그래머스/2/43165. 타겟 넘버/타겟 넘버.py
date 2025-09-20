

def solution(numbers, target):
    count = 0
    
    def dfs(depth, total):
        nonlocal count
        if depth == len(numbers):
            if total == target:
                count += 1
            return 
    
        dfs(depth + 1, total + numbers[depth])
        dfs(depth + 1, total - numbers[depth])
        
    dfs(0,0)
    return count
    