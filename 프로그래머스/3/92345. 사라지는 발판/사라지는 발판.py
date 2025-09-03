TURN_A = 1
TURN_B = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])

    def dfs(ax,ay,bx,by,turn):
        x,y = -1,-1
        if turn == TURN_A:
            x,y = ax,ay
        else:
            x,y = bx,by
        
        if board[x][y] == 0:
            return (False, 0)
        
        win_cases = []
        lose_cases = []
        
        board[x][y] = 0
        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny]:
                if turn == TURN_A:
                    result = dfs(nx,ny,bx,by,TURN_B)
                else:
                    result = dfs(ax,ay,nx,ny,TURN_A)
                if not result[0]: # 다음 플레이어가 진 경우 -> 내가 이김 
                    win_cases.append(result[1] + 1)
                else:
                    lose_cases.append(result[1] + 1)
        board[x][y] = 1 
        
        if win_cases: # 이긴 경우가 있는 경우 -> 이길 수 있으니 선택지 중 최소 거리의 선택을 해야됨
            return (True, min(win_cases))
        if lose_cases: # 이긴 경우가 하나도 없고 진 경우만 있을 경우 -> 앞으로 계속 질꺼니까 도망가야됨
            return (False, max(lose_cases))
        # 4방향의 다음 위치가 조건에 만족하지 않아 다음 경우의 수가 없을때
        return (False, 0)
        
        
    result = dfs(aloc[0], aloc[1], bloc[0], bloc[1], TURN_A)
    return result[1]
