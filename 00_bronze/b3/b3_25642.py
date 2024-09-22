# 젓가락 게임 - 25642

yt, yj = map(int, input().split())

while True:
    yj += yt
    if yj > 4:
        print("yt")
        break

    yt += yj
    if yt > 4:
        print("yj")
        break
