# 지폐 세기 - 30031

n = int(input())
sum_ = 0
for _ in range(n):
    width, _ = map(int, input().split())
    match width:
        case 136:
            sum_ += 1_000
        case 142:
            sum_ += 5_000
        case 148:
            sum_ += 10_000
        case 154:
            sum_ += 50_000
print(sum_)
