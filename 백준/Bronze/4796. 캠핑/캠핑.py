
case_num = 1
while True:
  l,p,v = map(int,input().strip().split())

  if l == 0 and p == 0 and v == 0:
    break

  periods = v // p
  remainings = v % p

  days = periods * l + min(remainings, l)

  print(f'Case {case_num}: {days}')

  case_num += 1