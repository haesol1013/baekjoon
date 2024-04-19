def find_fraction(x):
    diagonal_num = 1
    diagonal_sum = 0
    while diagonal_sum + diagonal_num < x:
        diagonal_sum += diagonal_num
        diagonal_num += 1

    if diagonal_num % 2 == 0:
        numerator = x - diagonal_sum
        denominator = diagonal_num - (x - diagonal_sum) + 1
    else:
        numerator = diagonal_num - (x - diagonal_sum) + 1
        denominator = x - diagonal_sum

    return f"{numerator}/{denominator}"

# 입력 받기
x = int(input())

# 결과 출력
print(find_fraction(x))
