def delete_card(a,b,total):
    for i in a:
        required = total - i
        if required in b:
            a.remove(i)
            b.remove(required)
            return True
    return False

def solution(coin, cards):
    answer = 1
    n = len(cards)
    mycard = cards[: n//3]
    idx = n // 3
    leftovers = []
    while coin >= 0 and idx < n:
        leftovers.append(cards[idx])
        leftovers.append(cards[idx + 1])
        idx += 2
        
        if delete_card(mycard, mycard, n + 1):
            pass
        elif coin >= 1 and delete_card(mycard, leftovers, n + 1):
            coin -= 1
        elif coin >= 2 and delete_card(leftovers,leftovers,n + 1):
            coin -= 2
        else:
            break
        answer += 1
    return answer
            