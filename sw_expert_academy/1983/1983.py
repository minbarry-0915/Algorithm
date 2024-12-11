
import sys
sys.stdin = open("input.txt", "r")

grade_list = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    score = []
    for i in range(N):
        mid, final, homework = map(int, input().split())
        total_score = mid * 0.35 + final * 0.45 + homework * 0.2
        score.append((total_score, i+1))
        
    score.sort(reverse=True, key=lambda x: x[0])
    
    grade_interval = N // 10
    
    for index, (score, student_num) in enumerate(score):
        if student_num == K:
            grade = grade_list[index // grade_interval]
            
    print(f'#{test_case} {grade}')
    # ///////////////////////////////////////////////////////////////////////////////////
'''
출처 : https://swexpertacademy.com/
'''