dice = list(map(int, input().split()))
dice.sort()
storage = [dice[0]]

for i in range(1, 3):
    if dice[i] == storage[0]:
        storage.append(dice[i])
    elif dice[i] > storage[0] and len(storage) < 2:
        storage[0] = dice[i]

if len(storage) == 3:
    money = 10000 + storage[0] * 1000
elif len(storage) == 2:
    money = 1000 + storage[0] * 100
else:
    money = storage[0] * 100

print(money)
