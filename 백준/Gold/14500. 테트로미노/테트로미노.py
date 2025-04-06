import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

shapes = ([(0, 0), (0, 1), (0, 2), (0, 3)],
          [(0, 0), (1, 0), (2, 0), (3, 0)],
          [(0, 0), (0, 1), (1, 0), (1, 1)],
          [(0, 0), (1, 0), (1, 1), (1, 2)],
          [(0, 0), (0, 1), (-1, 1), (-2, 1)],
          [(0, 0), (-1, 0), (-1, -1), (-1, -2)],
          [(0, 0), (0, -1), (1, -1), (2, -1)],
          [(0, 0), (-1, 0), (-1, 1), (-2, 1)],
          [(0, 0), (0, 1), (1, 1), (1, 2)],
          [(0, 0), (-1, 0), (-1, -1), (-2, -1)],
          [(0, 0), (0, 1), (-1, 1), (-1, 2)],
          [(0, 0), (0, 1), (0, 2), (1, 1)],
          [(0, 0), (-1, 0), (-1, 1), (-2, 0)],
          [(0, 0), (0, -1), (0, -2), (-1, -1)],
          [(0, 0), (1, 0), (1, -1), (2, 0)],
          [(0, 0), (1, 0), (1, -1), (1, -2)],
          [(0, 0), (0, 1), (1, 1), (2, 1)],
          [(0, 0), (-1, 0), (-1, 1), (-1, 2)],
          [(0, 0), (0, -1), (-1, -1), (-2, -1)]
          )


def calc(shape, x, y):
    total = 0
    for dx, dy in shape:
        nx = x + dx
        ny = y + dy

        if not (0 <= nx < n and 0 <= ny < m):
            return 0
        total += grid[nx][ny]

    return total


answer = 0
for i in range(n):
    for j in range(m):
        for shape in shapes:
            answer = max(answer, calc(shape, i, j))

print(answer)
