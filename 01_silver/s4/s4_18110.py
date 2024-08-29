# solved.ac - s4_18110

import sys
input = lambda: sys.stdin.readline().rstrip()


def round2(n: int | float) -> int:
    return int(n) if n - int(n) < 0.5 else int(n) + 1


def main():
    n = int(input())

    if n:
        arr = [int(input()) for _ in range(n)]
        cut = round2(n*0.15)

        sliced_arr = sorted(arr)[cut:n-cut]
        result = sum(sliced_arr)/len(sliced_arr)
        print(round2(result))
    else:
        print(0)


main()
