# 햄버거 정렬 - 32399

s = input()
match s:
    case "(1)":
        print(0)
    case ")1(":
        print(2)
    case _:
        print(1)
