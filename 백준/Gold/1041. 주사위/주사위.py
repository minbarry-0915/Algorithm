import sys

n = int(input())
arr = list(map(int,input().split()))

if n == 1:
    print(sum(arr) - max(arr))
    sys.exit()

answer = 0
min_arr = []
# 서로 마주보는 숫자 두개 중 작은값을 추가
min_arr.append(min(arr[0], arr[5]))
min_arr.append(min(arr[1], arr[4]))
min_arr.append(min(arr[2], arr[3]))
min_arr.sort()  # 오름차순 정렬

# 면이 1개 보이는 주사위, 2개 보이는 주사위, 3개 보이는 각 주사위의 면 최소합
sum1 = min_arr[0]
sum2 = min_arr[0] + min_arr[1]
sum3 = sum(min_arr)

side_one_count = (n - 2) ** 2 + ((n - 2) ** 2) * 4 + (n - 2) * 4
side_two_count = (n - 2) * 4 + (n - 2) * 4 + 4
side_three_count = 4

total = side_one_count * sum1 + side_two_count * sum2 + side_three_count * sum3
print(total)