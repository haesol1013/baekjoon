# 2007년 - 1924

extra_day = (3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3)
day = {0: "MON", 1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN"}
x, y = map(int, input().split())
days = sum(extra_day[:x-1]) + (y-1)
print(day[days % 7])
