# 행운의 바퀴 - 2840

import sys
input = lambda: sys.stdin.readline().rstrip()


n, k = map(int, input().split())
rullet = ["?"] * n

can_decide = True
point_index = 0
used_value = set()
for _ in range(k):
    move, input_value = input().split()
    move = int(move)
    point_index = (point_index+move) % n
    point_value = rullet[point_index]

    if point_value == "?":
        if input_value in used_value:
            can_decide = False
            break
        rullet[point_index] = input_value
        used_value.add(input_value)

    elif input_value != point_value:
        can_decide = False
        break

if can_decide:
    for i in range(n):
        print(rullet[point_index], end="")
        point_index = (point_index-1) % n
else:
    print("!")
