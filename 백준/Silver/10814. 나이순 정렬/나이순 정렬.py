N = int(input())
list_user_info = []

for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    list_user_info.append((age, name))

list_user_info.sort(key = lambda x: x[0])

for age, name in list_user_info:
    print(age,name)