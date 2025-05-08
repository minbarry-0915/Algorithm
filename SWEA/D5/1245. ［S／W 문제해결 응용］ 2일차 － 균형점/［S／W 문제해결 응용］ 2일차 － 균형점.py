T = int(input())
for t in range(1, T + 1):
    n = int(input())
    temp = list(map(int, input().split()))
    x = temp[:n] # 좌표
    m = temp[n:] # 질량
    
    # 전략
    # 두개씩 선택해서 좌우 인력이 일치하는 중간 지점을 탐색
    result = []
    for i in range(n - 1):
        left = x[i]
        right = x[i + 1]
        while right - left >= 1e-12:
            mid = (left + right) / 2
            left_force = right_force = 0
            for i in range(n):
                force = m[i] / (mid - x[i]) ** 2
                if x[i] < mid: # 왼쪽 힘이면
                    left_force += force
                else:
                    right_force += force
            if left_force < right_force: # 오른쪽힘이 더 세면 -> 오른쪽 기준점 낮추기
                right = mid
            else: # 왼쪽힘이 더 세면
                left = mid
        result.append(mid)

    print(f'#{t}', end=' ')
    print(' '.join('%.10f' %f for f in result))