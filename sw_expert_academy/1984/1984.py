import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    numbers = list(map(int, input().split()))
    # 최소값과 최대값 찾기
    curr_min = min(numbers)
    curr_max = max(numbers)
    
    numbers.remove(curr_min)
    numbers.remove(curr_max)

    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    
    result = round(sum / len(numbers))
    print(f'#{test_case} {result}')
    
    # ///////////////////////////////////////////////////////////////////////////////////
'''
출처 : https://swexpertacademy.com/
'''