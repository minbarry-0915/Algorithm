import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def update_count(grade_count, grade):
    if grade not in grade_count:
        grade_count[grade] = 1
    else:
        grade_count[grade] += 1
    
    
for test_case in range(1, T+1):
    test_case_number = int(input())
    grade_count = {}
    grades = list(map(int,input().split()))
    for grade in grades:
        update_count(grade_count, grade)
    
    max_count = max(grade_count, key=grade_count.get)
    
    print(f'#{test_case} {max_count}')