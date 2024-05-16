import sys


T = int(sys.stdin.readline())

for i in range(T):
    str_ = sys.stdin.readline().strip()
    print(str_[0] + str_[-1])
