T = int(input())

for testcase in range(1, T + 1):
    change = int(input())

    quarter = int(change // 25)
    change = change - quarter * 25

    dime = int(change // 10)
    change = change - dime * 10

    nickel = int(change // 5)
    change = change - nickel * 5

    penny = int(change // 1)

    print(quarter, dime, nickel, penny)
