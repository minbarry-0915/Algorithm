def solution(k, dungeons):
    n = len(dungeons)
    visited = [0] * n
    max_cnt = -1

    def dfs(tired, cnt):
        nonlocal max_cnt
        max_cnt = max(max_cnt, cnt)

        for i in range(n):
            if not visited[i]:
                need, use = dungeons[i]
                if tired >= need:
                    visited[i] = True
                    dfs(tired - use, cnt + 1)
                    visited[i] = False
    dfs(k, 0)
    return max_cnt