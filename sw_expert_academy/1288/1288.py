import sys
sys.stdin = open('input.txt', 'r')

T = int(input())



def check_all_numbers_true(numbers):
    return all(numbers.values())

def check_numbers(digits,numbers):
    for digit in digits:
        numbers[digit] = True


for test_case in range(1,T+1):
    N = int(input())
    
    numbers = {i: False for i in range(10)}
    
    count = 0
    while not check_all_numbers_true(numbers):
        count += 1 
        
        current_N = N * count
        digits = [int(digit) for digit in str(current_N)]   
        check_numbers(digits, numbers)    
    
    total = N * count
    
    print(f'#{test_case} {total}')