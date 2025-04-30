num = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

t = int(input())
for _ in range(t):
    t, n = map(str, input().split())
    n = int(n)
    n_lst = input().split()

    n_lst.sort(key= lambda x: num[x])

    print(t)
    print(*n_lst)