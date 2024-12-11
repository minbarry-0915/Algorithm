import sys
sys.stdin = open('input.txt','r')

T = 10



for test_case in range(1,T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    available = 0
    for i in range(2, N - 2):
        compare_lists = buildings[i-2: i+3] # i-2 부터 i + 2까지
        compare_lists.remove(buildings[i]) #기준 삭제
        
        max_height = max(compare_lists) #비교군중에 제일 높은 건물 찾기
        if max_height < buildings[i]: #제일 높은 건물이 기준 건물보다 낮으면
            available += buildings[i] - max_height #조망권확보 : 반영
    
        
    print(f'#{test_case} {available}')