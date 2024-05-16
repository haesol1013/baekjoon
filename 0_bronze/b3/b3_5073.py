while True:
    side = sorted(map(int, input().split()))
    s0, s1, s2 = side
    if s0 == s1 == s2 == 0:
        break
    elif s2 >= s0 + s1:
        result = "Invalid"
    elif s0 == s1 == s2:
        result = "Equilateral"
    elif s0 == s1 or s0 == s2 or s1 == s2:
        result = "Isosceles"
    else:
        result = "Scalene"
    print(result)
