n = int(input())
arr = list(map(int,input().split()))
arr.sort()

result = 0
for i in range(n - 2):
    start = i + 1
    end = n - 1
    while start < end:
        s = arr[start] + arr[end]
        if s == -arr[i]:
            # ex) [-7,1,1,1,1]
            if arr[start] == arr[end]:
                k = end - start + 1
                result += (k * (k - 1)) // 2
                break
            else:
                # ex) [-7,1,1,6,6,6]
                j,k = start, end
                while arr[start] == arr[j] and j < end:
                    j += 1
                while arr[end] == arr[k] and k > start:
                    k -= 1
                result += (j - start) * (end - k)
                start, end = j, k
        elif s < -arr[i]:
            start += 1
        else:
            end -= 1
print(result)