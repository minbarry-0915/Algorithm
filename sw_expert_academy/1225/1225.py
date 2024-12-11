import sys
sys.stdin = open('input.txt','r')

T = 10

def is_empty(array):
    return len(array) == 0

def enqueue(array,element):
    array.append(element)
    
def dequeue(array):
    if array is not is_empty(array):
        element = array[0]
        del array[0]
        return element
    return None
    
for test_case in range(1, T+1):
    case_num = int(input())
    
    digits = list(map(int, input().split()))
    
    while digits[-1] != 0:
        for i in range(1,6):    
            buffer = dequeue(digits)
            if buffer is not None:
                buffer -= i
                if buffer <= 0:
                    buffer = 0
                    enqueue(digits, 0)
                    break
                enqueue(digits, buffer)
                
                
    print(f'#{test_case} {" ".join(map(str, digits))}')