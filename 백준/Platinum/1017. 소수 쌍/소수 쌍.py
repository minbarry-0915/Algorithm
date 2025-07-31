N = int(input())
num_list = list(map(int, input().split()))

def is_prime(n) :
  if n == 2 :
    return True
  for i in range(2, int(n ** 0.5) + 1) :
    if n % i == 0 :
      return False
  return True

prime_list = [list() for _ in range(N)]

for i in range(N-1) :
  for j in range(i+1, N) :
    if is_prime(num_list[i] + num_list[j]) :
      prime_list[i].append(j)
      prime_list[j].append(i)

def bipartite_matching(idx) :
  matching = [-1]*N
  matching[0] = idx
  matching[idx] = 0

  def dfs(node) :
    if visited[node] :
      return False
    visited[node] = True
    for pair in prime_list[node] :
      if matching[pair] == -1 :
        matching[pair] = node
        matching[node] = pair
        return True
    for pair in prime_list[node] :
      if matching[pair] not in [0, idx] and dfs(matching[pair]) :
        matching[pair] = node
        matching[node] = pair
        return True
    return False

  result = 2
  for i in range(1, N) :
    if matching[i] == -1 :
      visited = [False]*N
      if dfs(i) :
        result += 2
  return result == N 

result = list()
for i in prime_list[0] :
  if bipartite_matching(i) :
    result.append(num_list[i])

if result :
  print(*sorted(result))
else :
  print(-1)