N = int(input())
schedules = []
max_count = 0
for _ in range(N):
    start, end = map(int, input().split())
    schedules.append((start, end))

# 종료시간 기준 정렬, 같은 종료시간일 경우 시작시간 기준
schedules.sort(key = lambda x: (x[1],x[0]))
current_end_time = 0

for start, end in schedules:
    if start >= current_end_time:
        max_count += 1
        current_end_time = end

print(max_count)