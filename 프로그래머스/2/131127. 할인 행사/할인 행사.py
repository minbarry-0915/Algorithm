from collections import Counter

def solution(want, number, discount):
    wanted = dict(zip(want, number))
    n = len(discount)
    # 슬라이딩 윈도우로 10개 뽑아내기
    answer = 0
    for i in range(0, n - 9):
        discounted = discount[i : i + 10]
        counter = Counter(discounted)
        
        if all (counter[item] >= wanted[item] for item in wanted):
            answer += 1
    return answer
