# ATM - 11399

def main():
    n = int(input())
    line = sorted(map(int, input().split()))

    prefix_sum = 0
    total = 0

    for i in line:
        prefix_sum += i
        total += prefix_sum

    print(total)


main()
