N = int(input())
#
# 2 - 7 : 2   6
# 8 - 19 : 3   12
# 20 - 37 : 4   18
# 38 - 62: 5 24
#
# N // 6 ==

def cal_num_room(N):
    if N == 1:
        return 1

    mini = 2
    maxi = 1
    n = 1
    while True:
        maxi = mini + n * 6 - 1

        if mini <= N <= maxi:
            return n + 1
                
        mini = maxi + 1
        n += 1

print(cal_num_room(N))


