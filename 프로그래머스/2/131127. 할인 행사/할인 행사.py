from collections import Counter

def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    answer = 0
    
    for i in range(len(discount) - 9):  # 10일씩 자르기 위해 -9
        window = discount[i:i + 10]
        counter = Counter(window)
        
        if all(counter[item] >= want_dict[item] for item in want_dict):
            answer += 1
            
    return answer
