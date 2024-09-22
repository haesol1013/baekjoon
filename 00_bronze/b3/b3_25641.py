# 균형 잡힌 소떡소떡 - 25641

from collections import deque

_ = input()
queue = deque(input())

while True:
    s, t = queue.count("s"), queue.count("t")
    if s == t:
        print("".join(queue))
        break
    else:
        queue.popleft()