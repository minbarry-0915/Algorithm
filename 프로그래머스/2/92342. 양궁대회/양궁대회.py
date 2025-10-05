def solution(n, info):
    best = [-1]
    best_diff = -1
    
    def calc_score(lion):
        apeach_score, lion_score = 0, 0
        for i in range(11):
            if info[i] == 0 and lion[i] == 0:
                continue
            if lion[i] > info[i]:
                lion_score += 10 - i
            else:
                apeach_score += 10 - i
        return lion_score - apeach_score
    
    def dfs(idx, arrow, lion):
        # 0점까지 모든 선택을 마쳤을때
        nonlocal best, best_diff
        if idx == 11:
            if arrow > 0: # 남은 화살이 있으면, 0점에 다 쏘는걸로 처리
                lion[10] += arrow
            diff = calc_score(lion)
            if diff > 0:
                if diff > best_diff: # 더 크면 초기화
                    best = lion[::]
                    best_diff = diff
                elif diff == best_diff and lion[::-1] > best[::-1]: # 가장 낮은 점수 맞힌갯수 > 그 다음 낮은 점수 맞힌 갯수 비교
                    best = lion[::]
            if arrow > 0:
                lion[10] -= arrow
            return
        
        
        # 이번 점수를 라이언이 쏠경우
        # 라이언은 본인이 점수를 얻어야하기 때문에 해당 판에서 이겨야됨
        # 어피치 보다 더 많이 쏴야됨
        need = info[idx] + 1
        if arrow - need >= 0:
            lion[idx] = need
            dfs(idx + 1, arrow - need, lion)
            lion[idx] = 0
        # 이번 점수를 라이언이 쏘지 않을 경우
        dfs(idx + 1, arrow, lion)            
    
    lion = [0] * 11
    dfs(0, n, lion)
    return best