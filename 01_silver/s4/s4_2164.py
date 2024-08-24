# 카드 2 - 2164

from collections import deque

n = int(input())
deck = deque(list(range(1, n+1)))
while len(deck) > 1:
    deck.popleft()
    deck.append(deck.popleft())
print(*deck)
