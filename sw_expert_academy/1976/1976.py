
import sys
sys.stdin = open("input.txt", "r")

def add_time(h1,m1,h2,m2):
    sum_h = h1 + h2
    sum_m = m1 + m2 
    total_min = sum_m % 60
    total_hr = (sum_h + (sum_m // 60)) % 12
    if total_hr == 0:
        total_hr = 12
    return total_hr, total_min
    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////
    h1, m1, h2, m2 = map(int, input().split())
    total_hr, total_min = add_time(h1,m1,h2,m2)
    
    print(f'#{test_case} {total_hr} {total_min}')
    # ///////////////////////////////////////////////////////////////////////////////////
'''
출처 : https://swexpertacademy.com/
'''