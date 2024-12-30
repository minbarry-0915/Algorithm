N = int(input())

X = list(map(int,input().split()))

sorted_X = sorted(set(X))

# ex)100: 1
rank_map = {value: index for index, value in enumerate(sorted_X)}

compressed_X = [rank_map[x] for x in X]

print(*compressed_X)