# 풍선 터뜨리기 - 2346

from collections import deque


def main():
    n = int(input())
    balloon = deque(enumerate(map(int, input().split())))
    log = []

    while balloon:
        idx, front = balloon.popleft()
        log.append(idx+1)
        rotate = front-1 if front > 0 else front
        balloon.rotate(-rotate)

    print(*log)


main()
