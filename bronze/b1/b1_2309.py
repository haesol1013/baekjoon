"""""""""
# 일곱 난쟁이
"""""""""

import sys

arr = [int(sys.stdin.readline().strip()) for _ in range(9)]

for i in range(0, len(arr)-1):
    for j in range(i+1, len(arr)):
        short1 = arr[i]
        short2 = arr[j]
        summation = sum(arr) - (short1+short2)
        if summation == 100:
            arr.remove(short1)
            arr.remove(short2)
            break

for i in sorted(arr):
    print(i)


# from itertools import combinations
# import sys
#
# arr = [int(sys.stdin.readline().strip()) for i in range(9)]
#
# for comb in combinations(arr, 7):
#     if sum(comb) == 100:
#         print("\n".join(map(str, sorted(comb))))
#         break
