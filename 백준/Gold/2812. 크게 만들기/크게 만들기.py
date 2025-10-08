n,k = map(int,input().split())
num_str = input().strip()

# 앞에서부터 큰 수를 남기는 방식
stack = []
for token in num_str:
    while stack and k > 0 and stack[-1] < token:
        stack.pop()
        k -= 1
    stack.append(token)
# k가 아직 남아 있으면 뒤에서부터 제거
while k > 0:
    stack.pop()
    k -= 1

print(''.join(stack))