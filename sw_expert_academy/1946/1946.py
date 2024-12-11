import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    doc = ""
    for _ in range(N):
        alphabet, count = input().split()
        count = int(count)
        
        doc += alphabet * count
        
    print(f"#{test_case}")
    for i in range(0, len(doc), 10):
        print(doc[i: i+10])
            
    
    