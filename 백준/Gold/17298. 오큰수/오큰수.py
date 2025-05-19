#import sys

#sys.stdin = open('input.txt', 'r', encoding='UTF-8')

n = int(input())
nums = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n - 1, - 1, -1):
    while stack and stack[-1] <= nums[i]:
        stack.pop()
    if stack: # 현재 지점보다 큰수발견
        answer[i] = stack[-1]
    stack.append(nums[i])
print(* answer)