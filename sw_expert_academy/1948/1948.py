import sys
sys.stdin = open("input.txt", "r")

T = int(input())

date = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

for test_case in range(1, T+1):
    month1, day1, month2, day2 = map(int, input().split())
    total = 0
    
    if month1 != month2:
        total = date[month1] - day1 + day2 + 1
        for month in range(month1+1, month2):
            total += date[month]
    else:
        total = day2 - day1 + 1        
    
    print(f"#{test_case} {total}")