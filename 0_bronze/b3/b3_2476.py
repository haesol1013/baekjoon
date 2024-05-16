import sys


n = int(input())
cash = []

for case in range(n):
    num_list = list(map(int, sys.stdin.readline().split()))
    num_set = list(set(num_list))
    length = len(num_set)

    if length == 1:
        result = num_list[0]
        cash.append(10000 + result*1000)

    elif length == 2:
        cnt = []

        for target in num_set:
            cnt.append(num_list.count(target))

        result = num_set[cnt.index(2)]
        cash.append(1000 + result*100)

    else:
        result = max(num_list)
        cash.append(result * 100)

print(max(cash))
