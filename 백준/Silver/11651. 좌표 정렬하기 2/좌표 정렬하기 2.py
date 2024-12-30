N = int(input())

coordinates = []
for _ in range(N):
    coordinates.append(tuple(map(int, input().split())))

coordinates.sort(key = lambda x: (x[1], x[0]))

for coordinate in coordinates:
    print(coordinate[0],coordinate[1])