while True:
  try:
    x = int(input()) * 10000000
    n = int(input())
    arr = list(int(input()) for _ in range(n))
    arr.sort()
    
    left = 0
    right = n - 1
    answer = []
    while left < right:
      if arr[left] + arr[right] < x:
        left += 1
      elif arr[left] + arr[right] > x:
        right -= 1
      else:
        answer = [arr[left], arr[right]]
        break
    
    if answer:
      print(f'yes {answer[0]} {answer[1]}')
    else:
      print('danger')
    
    
  
  except EOFError:
    break