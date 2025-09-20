def solution(numbers_str):
    numbers = set()
    n = len(numbers_str)
    visited = [False] * n
    
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    def dfs(current):
        if current:
            numbers.add(int(current))  
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(current + numbers_str[i])
                visited[i] = False
    
    dfs("")
    return sum(1 for num in numbers if is_prime(num))