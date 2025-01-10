T = int(input())
buttons = [300,60,10]
count = []

for button in buttons:
    count.append(T // button)
    T %= button

if T != 0:
    print(-1)
else:
    print(*count)

