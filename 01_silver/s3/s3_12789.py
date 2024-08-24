# 도키도키 간식드리미 - 12789


from collections import deque


def main():
    _ = input()
    li = deque(map(int, input().split()))
    print(get_answer(li))


def get_answer(li1: deque[int]) -> str:
    li2 = []
    i = 1

    while True:
        if not li1 and not li2:
            return "Nice"

        if li1 and li1[0] == i:
            li1.popleft()
            i += 1
        elif li2 and li2[-1] == i:
            li2.pop()
            i += 1
        elif li1:
            li2.append(li1.popleft())
        else:
            return "Sad"


main()
