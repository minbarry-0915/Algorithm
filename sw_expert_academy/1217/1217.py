import sys
sys.stdin = open('input.txt','r')

T = 10
for test_case in range(10):
    case_num = int(input())
    base, exp = map(int, input().split())
    
    sum = 1
    for i in range(exp):
        sum *= base
    
    print(f'#{case_num} {sum}')