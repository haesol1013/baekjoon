# 부녀회장이 될테야

import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    t = int(input())

    for _ in range(t):
        k = int(input())
        n = int(input())
        ans = [[0]*(n+1) for _ in range(k+1)]

        for i in range(1, n+1):
            ans[0][i] = i

        for i in range(1, k+1):
            for j in range(1, n+1):
                ans[i][j] = ans[i][j-1] + ans[i-1][j]

        print(ans[k][n])


main()

