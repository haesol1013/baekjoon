# FizzBuzz - 28702

import sys
input = lambda: sys.stdin.readline().rstrip()


def fizzbuzz(n: int) -> int | str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


def main():
    n = 0
    for i in range(3, 0, -1):
        x = input()
        if x not in ["Fizz", "Buzz", "FizzBuzz"]:
            n = int(x) + i
            break

    print(fizzbuzz(n))


if __name__ == "__main__":
    main()
