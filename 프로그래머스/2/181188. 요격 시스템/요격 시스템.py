def solution(targets):
    targets.sort(key = lambda x: [x[1], x[0]])
    
    answer = 0
    end = 0
    for t in targets:
        if t[0] >= end:
            end = t[1]
            answer += 1
    return answer