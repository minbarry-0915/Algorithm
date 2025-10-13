
import heapq

n,m = map(int,input().split())
students = []
heap = []
max_val = 0

for i in range(n):
    arr = list(map(int,input().split()))
    arr.sort()
    students.append(arr)
    max_val = max(max_val, arr[0])
    heapq.heappush(heap, (arr[0], i))

pointer = [0] * n

diff = int(1e9)
while heap:
    min_val, idx = heapq.heappop(heap)
    diff = min(diff, max_val - min_val)

    if pointer[idx] == m - 1:
        break
    pointer[idx] += 1
    heapq.heappush(heap, (students[idx][pointer[idx]], idx))
    max_val = max(max_val, students[idx][pointer[idx]])
print(diff)