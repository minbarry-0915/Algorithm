from collections import deque
def solution(rc, operations):
    n = len(rc)
    m = len(rc[0])

    rows = deque(deque(row[1:-1]) for row in rc)
    outline = [deque(rc[i][0] for i in range(n)), deque(rc[i][m - 1] for i in range(n))]
    
    for op in operations:
        if op == 'ShiftRow':
            # 바깥꺼는 각각 맨뒤에 있는 요소 앞으로 올리기
            outline[0].appendleft(outline[0].pop())
            outline[1].appendleft(outline[1].pop())
            # 행모음은 맨 뒤의 행 앞으로 올리기
            rows.appendleft(rows.pop())

        elif op == 'Rotate':
            # 바깥 열모음 왼쪽꺼의 첫번째 원소 => 행모음 첫번째 배열의 첫번째에 삽입
            rows[0].appendleft(outline[0].popleft())
            # 행모음 첫번째 배열의 마지막 원소 => 바깥 열모음 오른쪽꺼의 첫번째에 삽입
            outline[1].appendleft(rows[0].pop())
            # 바깥 열모음 오른쪽꺼의 마지막 원소 => 행모음 마지막 배열의 마직막에 삽입
            rows[-1].append(outline[1].pop())
            # 행모음 마지막 배열의 첫번째 원소 => 바깥 열모음 왼쪽꺼의 마지막에 삽입
            outline[0].append(rows[-1].popleft())

    
    answer = []
    for i in range(n):
        row = []
        row.append(outline[0][i])
        row.extend(rows[i])
        row.append(outline[1][i])
        answer.append(row)
    return answer