from collections import deque

N = int(input())

cards = deque(range(1, N+1))

while len(cards) > 1:
    cards.popleft()
    card = cards.popleft()
    cards.append(card)
    
print(cards[0])