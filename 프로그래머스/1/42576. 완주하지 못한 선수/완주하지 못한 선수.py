from collections import defaultdict
def solution(participant, completion):
    counter = defaultdict(int)
    
    for name in participant:
        counter[name] += 1
    
    for name in completion:
        counter[name] -= 1
    
    for name,count in counter.items():
        if count > 0:
            return name
    