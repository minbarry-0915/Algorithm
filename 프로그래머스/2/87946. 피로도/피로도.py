from itertools import permutations

def solution(k, dungeons):
    max_cnt = -1
    n = len(dungeons)

    for perm in permutations(dungeons, n):
        tired = k
        cnt = 0
        for need, use in perm:
            if tired >= need:
                tired -= use
                cnt+=1
            else:
                break
        max_cnt = max(max_cnt, cnt)
    return max_cnt