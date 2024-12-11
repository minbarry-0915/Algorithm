import sys
import argparse

def parseInputProcess_sssp(input_file):
    graph = {}
    # 입력 파일 열기
    with open(input_file, 'r') as f:
        # 탭 기준으로 쪼갬
        numVertices, numEdges, startVertex = map(int, f.readline().strip().split('\t'))
        # 정점 번호는 0부터 시작하므로 0부터 numVertices-1까지 초기화
        graph = {i: [] for i in range(numVertices)}
        
        # 간선 정보 읽기
        for _ in range(numEdges):
            u, v, weight = map(int, f.readline().strip().split('\t'))
            # undirected 그래프
            graph[u].append((v, weight))
            graph[v].append((u, weight))

    return numVertices, startVertex, graph

def dijkstra(numVertices, startVertex, graph):
    # 최소 비용 저장 용
    distances = {i: float('inf') for i in range(numVertices)}
    # 선행 노드 저장 용
    predecessors = {i: None for i in range(numVertices)}
    # 자기 자신한테 가는 최소 비용은 0
    distances[startVertex] = 0
    
    import heapq
    # 최소 힙 초기화
    priorityQueue = [(0, startVertex)] # 가중치, 시작노드
    
    while priorityQueue:
        currentDistance, currentVertex = heapq.heappop(priorityQueue)
        
        # 이미 입력되어 있는 값이 현재 노드의 거리보다 작다면, 끝난거
        if currentDistance > distances[currentVertex]:
            continue
        
        # 그래프에서 연결된 노드 탐색
        for neighbor, weight in graph[currentVertex]: 
            distance = currentDistance + weight
            # 입력되어 있는 값보다 짧은 거리 발견
            if distance < distances[neighbor]:
                #업데이트
                distances[neighbor] = distance
                predecessors[neighbor] = currentVertex
                # 가중치가 작은게 앞에 오게
                heapq.heappush(priorityQueue, (distance, neighbor))
    
    return distances,predecessors

# SSSP 결과를 출력하는 함수
def write_output_sssp(predecessors, output_file):
    with open(output_file, 'w') as f:
        for i, (vertex, predecessor) in enumerate(predecessors.items()):
            #마지막줄은 엔터 없이
            if i == len(predecessors) - 1:
                f.write(f'{vertex}\t{predecessor}')
            else:
                f.write(f'{vertex}\t{predecessor}\n')


def parseInput_floyd_warshall(input_file):
    with open(input_file,'r') as f:
        numVertices = int(f.readline().strip())
        #D: 최단 경로 가중치 행렬
        D_matrix = [list(map(int, f.readline().strip().split())) for _ in range(numVertices)]
        #P: precedessor matrix
        P_matrix = [[None if D_matrix[row][col] == 99999 or row == col else row + 1 for col in range(numVertices)] for row in range(numVertices)]
    return numVertices, D_matrix, P_matrix
        
def floyd_warshall(numVertices, D_matrix, P_matrix):
    for mid_node in range(numVertices):
        for start_node in range(numVertices):
            for end_node in range(numVertices):
                # 경유지와 연결되지 않은 경로는 무시
                if D_matrix[start_node][mid_node] == 99999 or D_matrix[mid_node][end_node] == 99999:
                    continue

                # 경유지를 통한 경로가 더 짧으면 업데이트
                weight = D_matrix[start_node][mid_node] + D_matrix[mid_node][end_node]
                if weight < D_matrix[start_node][end_node]:
                    D_matrix[start_node][end_node] = weight
                    # 경유지를 업데이트
                    if start_node != end_node:
                        P_matrix[start_node][end_node] = P_matrix[mid_node][end_node]
                
    return D_matrix, P_matrix


def write_output_apsp(D_matrix, P_matrix, numVertices, output_file_name):
    with open(output_file_name, 'w') as f:
        #D_matrix
        f.write(f'D\t{numVertices}\n')
        for row in D_matrix:
            f.write(f'\t'.join(str(x) for x in row) + '\n')
        #P_matrix
        f.write(f'P\t{numVertices}\n')
        for i, row in enumerate(P_matrix):
            if i == numVertices - 1:
                f.write(f'\t'.join("NIL" if x is None else str(x) for x in row))
            else:    
                f.write(f'\t'.join("NIL" if x is None else str(x) for x in row) + '\n')    

if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description= 'Process SSSP and APSP algorithms')
    parser.add_argument('input_sssp')
    parser.add_argument('input_apsp')
    parser.add_argument('output_sssp')
    parser.add_argument('output_apsp')
    #전달받은 인자 가지고 있는거임
    args = parser.parse_args()
    
    # SSSP 처리
    numVertices, startVertex, graph_sssp = parseInputProcess_sssp(args.input_sssp)
    distances, predecessors = dijkstra(numVertices, startVertex, graph_sssp)
    write_output_sssp(predecessors, args.output_sssp)
    
    # APSP 처리
    numVertices, D_matrix, P_matrix = parseInput_floyd_warshall(args.input_apsp)
    result_D_matrix, result_P_matrix = floyd_warshall(numVertices, D_matrix, P_matrix)
    write_output_apsp(result_D_matrix, result_P_matrix, numVertices, args.output_apsp)