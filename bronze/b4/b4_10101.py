"""""""""
# 삼각형 외우기
"""""""""

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

if angle1 + angle2 + angle3 == 180:
    if angle1 == angle2 == angle3:
        result = "Equilateral"

    elif (angle1 == angle2 or
          angle1 == angle3 or
          angle2 == angle3):
        result = "Isosceles"

    else:
        result = "Scalene"
else:
    result = "Error"

print(result)