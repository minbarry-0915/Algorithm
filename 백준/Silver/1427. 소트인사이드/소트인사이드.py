N = str(input())
number_list = list(int(number) for number in N)

number_list.sort(reverse=True)
print(''.join(map(str,number_list)))
    
