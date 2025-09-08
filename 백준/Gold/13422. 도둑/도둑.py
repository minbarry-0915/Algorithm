T = int(input())

for _ in range(T):
  # 집의 갯수, 연속으로 훔칠 집의 갯수, 알림 발생 최소 돈의 양
  n, m, k = map(int,input().split())
  
  houses = list(map(int,input().split()))
  
  cases = 0
  # 연속으로 훔칠 집을 고르되, k 보다 작아야됨
  # 고른 집이 이미 있는 경우면 세지 말아야됨
  # 합이 같아도 고른집이 다른 구성일 수 있음
  total = sum(houses[0: m])  
  if total < k:
    cases += 1
  
  total -= houses[0]
  total += houses[(0 + m) % n]
  
  if n != m:
    for i in range(1,n):
      if total < k:
        cases += 1
      total -= houses[i]
      total += houses[(i + m) % n]
  print(cases)