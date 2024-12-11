import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

numbers = {
    0: 'ZRO',
    1: 'ONE',
    2: 'TWO',
    3: 'THR',
    4: "FOR",
    5: "FIV",
    6: "SIX",
    7: "SVN",
    8: "EGT",
    9: "NIN",
}

numbers_dict = {v:k for k, v in numbers.items()}


for test_case in range(1, T+1):
    case_num, length = input().split()
    length = int(length)
    
    num = list(input().split())
    
    key_array = []
    for i in range(length):
        key_array.append(numbers_dict[num[i]])
    
    key_array.sort()
    for i in range(length):
        for key,value in numbers_dict.items():
            if value == key_array[i]:
                key_array[i] = key
    
    print(f'{case_num} {" ".join(map(str, key_array))}')