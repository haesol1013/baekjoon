# Run-Length Encoding! Run! - 16634

import sys
input = lambda: sys.stdin.readline().rstrip()


order, s = input().split()


def encode(s: str) -> str:
    result = [s[0]]
    cnt = 1
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            cnt += 1
        else:
            result.append(str(cnt))
            result.append(s[i])
            cnt = 1
    result.append(str(cnt))
    return "".join(result)


def decode(s: str) -> str:
    result = []
    for i in range(0, len(s), 2):
        result.append(s[i] * int(s[i+1]))
    return "".join(result)


if order == "E":
    print(encode(s))
else:
    print(decode(s))
