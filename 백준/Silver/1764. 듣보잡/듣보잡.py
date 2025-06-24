n,m = map(int,input().split())
even_listen = set()
even_seen = set()

for _ in range(n):
    name = input().strip()
    even_listen.add(name)

for _ in range(m):
    name = input().strip()
    even_seen.add(name)

intersect = even_seen & even_listen
lst_intersect = sorted(list(intersect))

print(len(intersect))
for name in lst_intersect:
    print(name)
