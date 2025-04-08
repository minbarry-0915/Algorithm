import sys
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
dragons = [tuple(map(int, input().split())) for _ in range(n)]

grid = [[0] * 101 for _ in range(101)]

# → ↑ ← ↓ (문제 기준)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(direction_list, depth, generation):
    if depth == generation:
        return direction_list

    new_dirs = []
    for d in reversed(direction_list):
        new_dirs.append((d + 1) % 4)

    new_direction_list = direction_list + new_dirs
    return dfs(new_direction_list, depth + 1, generation)

for x, y, d, g in dragons:
    grid[y][x] = 1
    directions = dfs([d], 0, g)

    for dir in directions:
        x += dx[dir]
        y += dy[dir]
        if 0 <= x < 101 and 0 <= y < 101:
            grid[y][x] = 1

count = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i + 1][j] and grid[i][j + 1] and grid[i + 1][j + 1]:
            count += 1

print(count)
