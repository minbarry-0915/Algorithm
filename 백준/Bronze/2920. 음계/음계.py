numbers = list(map(int, input().split()))

ascending = [i for i in range(1, 9)]
descending = list(reversed(ascending))  # 올바른 역순 리스트 생성

if numbers == ascending:
    print('ascending')
elif numbers == descending:
    print('descending')
else:
    print('mixed')
