def dfs(depth, lst, n, visited):
    global answer
    if depth == chance:
        answer = max(answer, int(''.join(lst)))
        return

    for i in range(n - 1):
        for j in range(i + 1, n):
            lst[i], lst[j] = lst[j], lst[i]

            char = ''.join(lst)
            if (depth + 1, char) not in visited:
                visited.add((depth + 1, char))
                dfs(depth + 1, lst, n, visited)

            lst[i], lst[j] = lst[j], lst[i]  # 백트래킹

T = int(input())
for t in range(1, T + 1):
    buffer = input().split()
    num_lst = list(buffer[0])  # 문자열 리스트
    n = len(num_lst)
    chance = int(buffer[1])
    answer = 0
    visited = set()
    dfs(0, num_lst, n, visited)
    print(f"#{t} {answer}")
