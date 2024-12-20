X = int(input())
N = int(input())
total_price = 0
for i in range(N):
    price, count = map(int, input().split())
    total_price += price * count
    
if total_price != X:
    print('No')
else:
    print('Yes')