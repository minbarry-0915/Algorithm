n = int(input())
k = int(input())
arr = list(map(int,input().split()))
arr.sort()
diff = [arr[i + 1] - arr[i] for i in range(n - 1)]
diff.sort(reverse=True)
print(sum(diff[k - 1:]))