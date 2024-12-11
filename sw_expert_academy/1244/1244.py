import sys
sys.stdin = open('input.txt', 'r')

def dfs(n):
    global answer
    if n == N:  # 최대 교환 횟수에 도달했으면
        answer = max(answer, int("".join(map(str, lst))))
        return        
    
    for i in range(L - 1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]  # 자리 교환
            
            chk = int("".join(map(str, lst)))
            if (n + 1, chk) not in v:  # 다음 교환 횟수와 현재 조합 확인
                v.add((n + 1, chk))  # 방문한 조합 추가
                dfs(n + 1)  # 다음 단계로 진행

            lst[j], lst[i] = lst[i], lst[j]  # 자리 복구

T = int(input())

for test_case in range(1, T + 1):
    st, t = map(str, input().split())
    N = int(t)
    lst = list(st)  # 입력 문자열을 리스트로 변환
    v = set()  # 방문 기록을 집합으로
    L = len(st)
    answer = 0
    dfs(0)  # DFS 시작
    print(f'#{test_case} {answer}')  # 결과 출력
