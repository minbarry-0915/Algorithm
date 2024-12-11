import sys
sys.stdin = open('input.txt','r')

def is_palindrome(word):
    return word == word[::-1]

T = 10

for test_case in range(1,T+1):
    case_num = int(input())
    matrix = [list(input().strip()) for _ in range(100)]
    
    max_len = 1
    for row in range(100):
        for start in range(100):
            for end in range(start+ 1, 101):
                target = matrix[row][start:end]
                result = is_palindrome(target)
                if result:
                    max_len = max(max_len, len(target))
                        
    for col in range(100):
        for start in range(100):
            for end in range(start + 1, 101):
                target = [matrix[row][col] for row in range(start, end)]
                result = is_palindrome(target)
                if result:
                    max_len = max(max_len, len(target))
                        
    print(f'#{case_num} {max_len}')
    