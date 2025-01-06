cost = int(input())

change = 1000 - cost

count = 0
currencies = [500,100,50,10,5,1]

for currency in currencies:
    count += change // currency
    change = change % currency
    
print(count)