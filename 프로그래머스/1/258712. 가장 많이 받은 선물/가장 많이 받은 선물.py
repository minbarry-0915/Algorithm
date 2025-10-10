def solution(friends, gifts):
    name_to_idx = {}
    n = len(friends)
    for i in range(n):
        name_to_idx[friends[i]] = i

    # print(name_to_idx)    
    
    # 선물 기록
    present_count = [[0] * n for _ in range(n)]
    # 선물 지수 저장
    present_indices = {i:0 for i in range(n)}
    
    # 선물 기록 반영
    for g in gifts:
        frm, to = g.split()
        present_count[name_to_idx[frm]][name_to_idx[to]] += 1
    # print(present_count)
    # 선물 지수 계산
    for i in range(n):
        outcome_count = sum(present_count[i][idx] for idx in range(n) if idx != i)
        income_count = sum(present_count[idx][i] for idx in range(n) if idx != i)
        present_indices[i] = outcome_count - income_count
    
    # 다음달 선물 계산
    additional_present_count = [0] * n # 받는거만 알면 됨
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if present_count[i][j] > present_count[j][i]:
                additional_present_count[i] += 1
            elif present_count[i][j] < present_count[j][i]:
                additional_present_count[j] += 1
            elif present_count[i][j] == present_count[j][i] or present_count[i][j] == 0:
                if present_indices[i] > present_indices[j]:
                    additional_present_count[i] += 1
                elif present_indices[i] < present_indices[j]:
                    additional_present_count[j] += 1
    # 두번씩 반복되므로 2로 나눔
    for i in range(n):
        additional_present_count[i] //= 2
   
    answer = max(additional_present_count)
    return answer