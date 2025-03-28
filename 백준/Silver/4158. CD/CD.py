import sys
import bisect

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    jack = [int(input()) for _ in range(n)]
    jill = [int(input()) for _ in range(m)]

    count = 0
    for cd in jack:
        if bisect.bisect_left(jill, cd) < len(jill) and jill[bisect.bisect_left(jill, cd)] == cd:
            count += 1

    print(count)
