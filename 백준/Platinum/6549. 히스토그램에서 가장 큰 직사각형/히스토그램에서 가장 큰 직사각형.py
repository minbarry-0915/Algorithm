# import sys
# sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def find_largest_rectangle(hist, n):
    stack = []
    idx = 0
    max_area = 0
    
    while idx < n:
        if not stack or hist[stack[-1]] < hist[idx]:  # 현재 최대 높이보다 큰애 발견
            stack.append(idx)
            idx += 1
        else:
            top = stack.pop()
            width = idx if not stack else idx - stack[-1] - 1
            area = hist[top] * width
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        width = idx if not stack else idx - stack[-1] - 1
        area = hist[top] * width
        max_area = max(max_area, area)
    return max_area

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        exit()
    n, hist = nums[0], nums[1:]
    print(find_largest_rectangle(hist, n))
