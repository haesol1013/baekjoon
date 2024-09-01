# 집합 - 11723

import sys
input = lambda: sys.stdin.readline().rstrip()


def modifier(set_: set, order: str, val: int) -> set:
    match order:
        case "add":
            if val not in set_:
                set_.add(val)
        case "remove":
            if val in set_:
                set_.remove(val)
        case "check":
            print(1 if val in set_ else 0)
        case "toggle":
            if val in set_:
                set_.remove(val)
            else:
                set_.add(val)
        case "all":
            set_ = set(range(1, 21))
        case "empty":
            set_.clear()
    return set_


def main():
    m = int(input())
    set_ = set()

    for _ in range(m):
        order = input().split()

        val = int(order[1]) if len(order) == 2 else None
        set_ = modifier(set_, order=order[0], val=val)


main()
