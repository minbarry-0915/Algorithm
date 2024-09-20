def insertion_sort(array):
    array_copy = array[:]
    
    for j in range(1, len(array_copy)):  # j를 1부터 시작
        key = array_copy[j]
        i = j - 1
        while i >= 0 and array_copy[i] > key:  # i가 0 이상일 때까지
            array_copy[i + 1] = array_copy[i]
            i -= 1
        array_copy[i + 1] = key

  
    return array_copy
    
def merge(array, p, q, r):
    n1 = q - p + 1  # 첫 번째 서브배열 요소 개수
    n2 = r - q      # 두 번째 서브배열 요소 개수

    # 배열 생성
    L = [0] * n1
    R = [0] * n2

    # 서브배열 L과 R에 값 복사
    for i in range(n1):
        L[i] = array[p + i]
    for j in range(n2):
        R[j] = array[q + 1 + j]

    # 병합 과정
    i = 0  # L의 인덱스
    j = 0  # R의 인덱스

    for k in range(p, r + 1):  # r + 1까지 반복
        if i < n1 and (j >= n2 or L[i] <= R[j]):
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
    
def merge_sort(array, p, r):
    if p < r:
        q = (p + r) // 2  # q: 리스트 중앙
        merge_sort(array, p, q)  # 처음부터 중앙까지
        merge_sort(array, q + 1, r)  # 중앙부터 끝까지
        merge(array, p, q, r)

def merge_insertion_sort(array, p, r, k):
    '''
    p: 시작점
    r: 종료점
    k: 서브 리스트 최소단위
    '''
    if r - p + 1 <= k:  # 서브리스트의 크기가 k보다 작으면 삽입 정렬 수행
        sorted_sublist = insertion_sort(array[p:r+1])
        for i in range(len(sorted_sublist)):
            array[p + i] = sorted_sublist[i]
    
    if p < r: #최소 단위로 쪼갬
        q = (p + r) // 2  # q: 리스트 중앙
        merge_insertion_sort(array, p, q, k)  # 왼쪽 서브리스트 정렬
        merge_insertion_sort(array, q + 1, r, k)  # 오른쪽 서브리스트 정렬
        merge(array, p, q, r)  # 병합

def write(array, mode='w'):
    with open("output.txt", mode) as outfile:
        outfile.write(" ".join(map(str, array)))
        
def enter():
    with open("output.txt", 'a') as outfile:
        outfile.write("\n")  # 줄바꿈 추가
        
def process_input_output():
    with open("input.txt", "r") as infile:
        lines = infile.readlines()
        n = int(lines[0].strip())  # 배열 크기
        array = list(map(int, lines[1].strip().split()))
    
    #insertion_sort 
    sorted_array = insertion_sort(array)
    write(sorted_array)  # 삽입 정렬 결과 저장
    enter()
    print("insertion sorting done")  
    
    #merge_sort
    sorted_merge = array[:]  # 원본 배열의 복사본
    merge_sort(sorted_merge, 0, len(sorted_merge) - 1)  # 정렬 수행
    write(sorted_merge, mode='a')  # 병합 정렬 결과 추가로 저장
    enter()
    print("merge sorting done")

    #merge_insertion_sort
    k = 3  # 삽입 정렬을 적용할 최소 서브리스트 크기
    sorted_merge_insertion = array[:]
    merge_insertion_sort(sorted_merge_insertion, 0, len(array) - 1, k)  # 병합-삽입 정렬 수행
    write(sorted_merge_insertion, mode='a')  # 정렬 결과 저장
    print("merge insertion sort done")

process_input_output()
