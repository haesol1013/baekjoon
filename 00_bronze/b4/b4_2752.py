# 세수정렬 - 2752

import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    arr = list(map(int, input().split()))
    print(*sorted(arr))


if __name__ == "__main__":
    main()
