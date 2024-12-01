# On the Bus - 7582

import sys
input = lambda: sys.stdin.readline().rstrip()


while True:
    route, max_p = input().split()
    max_p = int(max_p)

    if route == "#" and max_p == 0:
        break
    
    curr_p = int(input())
    repeat = int(input())
    for _ in range(repeat):
        off, on = map(int, input().split())
        curr_p = min(curr_p + on - off, max_p)
    
    print(route, curr_p)
