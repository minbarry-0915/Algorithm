def get_quad_tree(x, y, size, grid):
    # 모든 값이 동일한지 확인
    base = grid[x][y]
    all_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if grid[i][j] != base:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        return base

    # 네 구역으로 쪼개서 재귀 호출
    sub_size = size // 2
    top_left = get_quad_tree(x, y, sub_size, grid)
    top_right = get_quad_tree(x, y + sub_size, sub_size, grid)
    bottom_left = get_quad_tree(x + sub_size, y, sub_size, grid)
    bottom_right = get_quad_tree(x + sub_size, y + sub_size, sub_size, grid)

    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# 입력 받기
n = int(input())
grid = [list(input().strip()) for _ in range(n)]

# 출력
print(get_quad_tree(0, 0, n, grid))
