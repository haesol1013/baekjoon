# 에디터 - 1406

import sys
input = lambda: sys.stdin.readline().rstrip()


arr_l = list(input())
arr_r = []
m = int(input())

for _ in range(m):
    order = list(input().split())
    match order[0]:
        case "L":
            if arr_l:
                arr_r.append(arr_l.pop())
        case "D":
            if arr_r:
                arr_l.append(arr_r.pop())
        case "B":
            if arr_l:
                arr_l.pop()
        case "P":
            arr_l.append(order[1])

print("".join(arr_l + list(reversed(arr_r))))
