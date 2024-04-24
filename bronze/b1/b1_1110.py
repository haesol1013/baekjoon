"""""""""
# 더하기 사이클
"""""""""
n = int(input())
i = 1
new_n = n

while True:
    str_n = str(new_n)

    if len(str_n) == 1:
        str_n = '0' + str_n

    result = int(str_n[0]) + int(str_n[-1])
    new_n = int(str_n[1] + str(result)[-1])

    if n == new_n:
        break
    else:
        i += 1

print(i)
