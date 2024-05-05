# 스택 - 10828

import sys


def stack(order: str):
    global arr
    n = None
    order = order.rstrip()

    if " " in order:
        order, n = order.split()

    match order:
        case ("push"):
            arr.append(n)
        case ("pop"):
            return arr.pop() if arr else "-1"
        case ("size"):
            return str(len(arr))
        case ("empty"):
            return "0" if arr else "1"
        case ("top"):
            return arr[-1] if arr else "-1"


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    order = sys.stdin.readline()
    result = stack(order)

    if result:
        print(result)
