import sys
sys.setrecursionlimit(10**4)
def find(x,parent):
  if parent[x] != x:
    parent[x] = find(parent[x],parent)
  return parent[x]
  
def union(a,b,parent,on_cycle) :
  a_root,b_root = find(a,parent), find(b,parent)
  if a_root != b_root:
    parent[b_root] = a_root # 트리로 묶고
    on_cycle[a_root] |= on_cycle[b_root] # 사이클 여부도 가져옴
  else: # 부모가 같으면 둘이 연결시 사이클 생성됨
    on_cycle[a_root] = True
    
case_no = 1
while True:
  n,m = map(int,input().split())
  if (n,m) == (0,0):
    break
  
  # 유니온 - 파인드
  parent = list(range(n + 1))
  on_cycle = [False] * (n + 1)
  for _ in range(m):
    a,b = map(int,input().split())
    union(a,b,parent,on_cycle)
  
  # 트리 갯수 계산
  roots = set(find(i, parent) for i in range(1, n+1))
  tree_count = sum(1 for r in roots if not on_cycle[r])
  
  # 출력
  print(f'Case {case_no}:', end=' ')
  if tree_count > 1:
    print(f'A forest of {tree_count} trees.')
  elif tree_count == 1:
    print(f'There is one tree.')
  else:
    print('No trees.')
  case_no += 1