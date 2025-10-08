import sys
import heapq
# sys.stdin = open('input.txt','r')

n = int(input())
schedules = list(tuple(map(int,input().split())) for _ in range(n))
schedules.sort(key=lambda x: x[0])

heap = []
for start, end in schedules:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)
print(len(heap))