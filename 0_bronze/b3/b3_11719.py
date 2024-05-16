# 그대로 출력하기 2 - 11719

while True:
    try:
        word = input()
        print(word)
    except EOFError:
        break
