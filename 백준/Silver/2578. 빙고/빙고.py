
def check_visit(visited, target):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == target:
                visited[i][j] = 1

def check_bingo(visited):
    line = 0

    for row in visited:
        if all(row):
            line += 1

    for col in range(5):
        if all(visited[row][col] for row in range(5)):
            line += 1

    if all(visited[i][i] for i in range(5)):
        line += 1

    if all(visited[i][4 - i] for i in range(5)):
        line += 1

    if line >= 3:
        return True
    else:
        return False
######

grid = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * (5) for _ in range(5)]
targets = []
for _ in range(5):
    target_lst = list(map(int,input().split()))
    for target in target_lst:
        targets.append(target)

answer = 1
while targets:
    target = targets.pop(0)
    check_visit(visited, target)
    result = check_bingo(visited)
    if result: # 빙고이면
        break
    else:
        answer += 1
print(answer)

