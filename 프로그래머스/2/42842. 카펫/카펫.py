def solution(brown, yellow):
    # 세로가 3이상 가로가 3이상이여야 둘러쌀수 있음
    # 더해서 x * y = 전체 격자 수가 되는 경우의 수를 찾아서 시도
    # 브라운 경로 돌려서 갯수 센다음에비교했을때 일치하면 x,y 리턴
    
    total = brown + yellow
    for h in range(3, total + 1):
        if total % h == 0:
            w = total // h
            if w >= h and (w - 2) * (h - 2) == yellow:
                return [w,h]