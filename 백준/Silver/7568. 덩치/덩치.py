N = int(input())
people = []
for _ in range(N):
    x,y = map(int, input().split())
    people.append((x,y))


res = []
for x1,y1 in people:
    rank = 1
    for x2,y2 in people:
        if x1 < x2 and y1 < y2:
            rank += 1
    res.append(rank)
    
print(*res)