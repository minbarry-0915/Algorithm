import sys
import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

total_cost = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum_val = a + b

    total_cost += sum_val
    heapq.heappush(cards, sum_val)
    
print(total_cost)