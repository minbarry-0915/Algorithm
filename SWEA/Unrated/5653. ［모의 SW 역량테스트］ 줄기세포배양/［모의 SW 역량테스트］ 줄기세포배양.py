import heapq

dy = [0,0,1,-1]
dx = [1,-1,0,0]

DEAD = 0
ACTIVE = 1
INACTIVE = 2

class Cell:
    def __init__(self, x, y, time, power):
        self.x = x
        self.y = y
        self.time = time   # 상태 전환/죽음 시간
        self.power = power
        self.state = INACTIVE

    def __lt__(self, other):
        # heapq는 min-heap이므로 power 큰 순서로 나오게 음수 사용
        return self.power > other.power

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def simulation(K, initial_cells):
    cells = set()
    heap = []

    # 초기 세포 배치
    for (x, y, p) in initial_cells:
        c = Cell(x, y, p, p)
        cells.add(c)

    for cur_time in range(1, K+1):
        while heap:
            c = heapq.heappop(heap)
            cells.add(c)

        # 모든 세포 상태 업데이트
        for c in cells:
            if c.state == DEAD:
                continue
            elif c.state == INACTIVE and c.time == cur_time:
                c.state = ACTIVE
                c.time = cur_time + c.power  # 죽는 시간

                # 번식
                for d in range(4):
                    nx = c.x + dx[d]
                    ny = c.y + dy[d]
                    heapq.heappush(heap, Cell(nx, ny, cur_time + 1 + c.power, c.power))

            elif c.state == ACTIVE and c.time == cur_time:
                c.state = DEAD

    # 살아있는 세포 카운트
    return sum(1 for c in cells if c.state in (INACTIVE, ACTIVE))


# 입력 처리 예시
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    initial_cells = [list(map(int, input().split())) for _ in range(N)]
    cells_list = []
    for i in range(N):
        for j in range(M):
            if initial_cells[i][j] > 0:
                cells_list.append((i, j, initial_cells[i][j]))
    ans = simulation(K, cells_list)
    print(f"#{tc} {ans}")