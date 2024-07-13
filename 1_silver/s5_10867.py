# 중복 빼고 정렬하기 - 10867

import sys

n = int(sys.stdin.readline())
arr = map(int, sys.stdin.readline().split())
print(*sorted(set(arr)))
