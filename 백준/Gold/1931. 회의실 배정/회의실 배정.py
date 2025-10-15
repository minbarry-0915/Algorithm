n = int(input())
timetable = [tuple(map(int,input().split())) for _ in range(n)]
timetable.sort(key= lambda x: (x[1],x[0]))

current_end_time = 0
cnt = 0

for start, end in timetable:
    if start >= current_end_time:
        cnt += 1
        current_end_time = end
print(cnt)