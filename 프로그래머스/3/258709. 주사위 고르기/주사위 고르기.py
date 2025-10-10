from collections import Counter

def solution(dices):
    n = len(dices)
    half = n // 2
    answer = []
    total_cases = (6 ** half) ** 2
    
    def get_combinations(user_dices):
        sums = Counter()
        def dfs(depth, total):
            if depth == half:
                sums[total] += 1
                return
            for num in user_dices[depth]:
                dfs(depth + 1, total + num)
            return
        dfs(0,0)
        return sums
    
    def simulation(A_indices, B_indices):
        A_dices = [dices[i] for i in A_indices]
        B_dices = [dices[i] for i in B_indices]
        
        A_combinations = get_combinations(A_dices)
        B_combinations = get_combinations(B_dices)
        
        # 정렬후 prefix
        sorted_B = sorted(B_combinations.items())
        prefix_B = []
        total = 0
        for s, cnt in sorted_B:
            total += cnt
            prefix_B.append((s,total))
        
        # A의 각 선택에 따른 이분 탐색 시작
        A_total_wins = 0
        for s, cnt in A_combinations.items():
            left = 0
            right = len(prefix_B) - 1
            A_wins = 0
            while left <= right:
                mid = (left + right) // 2
                if prefix_B[mid][0] < s:
                    A_wins = prefix_B[mid][1]
                    left = mid + 1
                else:
                    right = mid - 1
            A_total_wins += A_wins * cnt
            
        # 케이스 점수 계산
        win_rate = A_total_wins / total_cases
        answer.append((A_indices[:], win_rate))
            
    
    def choose_A_dices(depth, start, A_indices):
        if depth == half:
            B_indices = [i for i in range(n) if i not in A_indices]
            simulation(A_indices, B_indices)
            return
        
        for i in range(start, n):
            A_indices.append(i)
            choose_A_dices(depth + 1, i + 1, A_indices)
            A_indices.pop()
        return
    
    choose_A_dices(0, 0, [])
    # 정리
    best = max(answer, key = lambda x: x[1])
    
    return sorted([num + 1 for num in best[0]])
