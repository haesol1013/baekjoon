# 패리티 - 4579

while True:
    s = input()
    if s == "#":
        break
    is_odd = s[:-1].count("1") % 2
    print(s[:-1], end="")
    if s[-1] == "e":
        if is_odd:
            print("1")
        else:
            print("0")
    else:
        if is_odd:
            print("0")
        else:
            print("1")
