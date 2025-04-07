import sys

#sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n  # 팀 가르기
answer = int(1e9)


def dfs(depth, idx):
    global answer
    if depth == n // 2:
        team_start = 0
        team_link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j] and i != j:
                    team_start += s[i][j]
                elif not visited[i] and not visited[j] and i != j:
                    team_link += s[i][j]
        answer = min(answer, abs(team_start - team_link))
        return 
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0,0)
print(answer)