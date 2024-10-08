import random
import sys
import copy

sys.stdin = open('input.txt', 'r')

def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    
    return i + 1

def naive_quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)  # 피벗의 최종 위치
        naive_quick_sort(array, p, q - 1)  # 왼쪽 부분 정렬
        naive_quick_sort(array, q + 1, r)  # 오른쪽 부분 정렬
        
def randomized_partition(array, p ,r):
    rand_index = random.randint(p, r)
    array[rand_index], array[r] = array[r], array[rand_index]  # 피벗을 배열의 끝으로 이동
    
    return partition(array, p, r)

def randomized_partition_with_median(array, p, r):
    # 3개의 무작위 값 선택
    random_indices = random.sample(range(p, r + 1), 3)  # p에서 r까지의 인덱스 중 무작위로 3개 선택
    
    random_values = [array[i] for i in random_indices]  # 샘플링한 인덱스에 해당하는 값
    random_values.sort()
    median_value = random_values[1]  # 중간값

    # median_value의 원래 배열에서의 인덱스를 찾기
    median_index = random_indices[random_values.index(median_value)]

    # 중간값을 배열의 끝으로 이동
    array[median_index], array[r] = array[r], array[median_index]
    
    return partition(array, p, r)

        
def randomized_quick_sort(array, p, r, mode='default'):
    if p < r:
        if mode == 'default':
            q = randomized_partition(array, p, r)  # 기본 랜덤 파티션 호출
        elif mode == 'median' and (r - p >= 3): #최소 원소 갯수 보장
            q = randomized_partition_with_median(array, p, r)  # 중간값 파티션 호출
        else:
            q = randomized_partition(array, p, r)  # 기본 랜덤 파티션으로 대체
        
        randomized_quick_sort(array, p, q - 1, mode)  # 왼쪽 부분 정렬
        randomized_quick_sort(array, q + 1, r, mode)  # 오른쪽 부분 정렬

            

def write(array, mode='w'):
    with open("output.txt", mode) as outfile:
        outfile.write(" ".join(map(str, array)))  # 정렬된 결과를 파일에 기록
        
def enter():
    with open("output.txt", 'a') as outfile:
        outfile.write("\n")  # 줄바꿈 추가

def process_input_output():
    N = int(input())  # 배열의 크기 입력
    numbers = list(map(int, input().strip().split()))  # 정렬할 숫자 입력

    # numbers의 복사본을 생성하여 작업
    sorted_numbers = copy.deepcopy(numbers)  # 깊은 복사로 새로운 배열 생성
    # naive_quick_sort
    naive_quick_sort(sorted_numbers, 0, N - 1)  # 복사된 배열을 퀵 정렬 호출
    write(sorted_numbers)  # 정렬된 결과를 output.txt에 저장
    enter()
    
    # randomized_quick_sort
    sorted_numbers_2 = copy.deepcopy(numbers)
    randomized_quick_sort(sorted_numbers_2, 0, N - 1, mode='default')
    write(sorted_numbers_2, mode='a') # a: 이어 쓰기
    enter()
    
    # randomized_quick sort (median of 3)
    sorted_numbers_3 = copy.deepcopy(numbers)
    randomized_quick_sort(sorted_numbers_3, 0, N - 1, mode='median')
    write(sorted_numbers_3, mode='a')
        

# 프로그램 실행
process_input_output()
