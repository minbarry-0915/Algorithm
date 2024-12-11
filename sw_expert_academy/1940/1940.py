import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    current_speed = 0
    total_distance = 0 
    
    
    for _ in range(N):
        command = list(map(int, input().split()))
        
        
        if command[0] == 0:
            # 현재 속도 유지
            distance = current_speed
        elif command[0] == 1:
            # 가속
            acceleration = command[1]
            current_speed += acceleration
            distance = current_speed
        elif command[0] == 2:
            # 감속
            deceleration = command[1]
            current_speed -= deceleration
            
            # 현재 속도보다 감속할 속도가 더 클 때 , ex) current = 0, 감속= 1
            if current_speed < 0:
                current_speed = 0
            distance = current_speed
            
        total_distance += distance   
        
    
    print(f'#{test_case} {total_distance}')