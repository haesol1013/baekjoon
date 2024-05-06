# Hashing - 15829

length = int(input())
sequence = input()
alphabet = "_abcdefghijklmnopqrstuvwxyz"
summation = 0
for i in range(length):
    index = alphabet.index(sequence[i])
    summation += index * 31**i
print(summation % 1234567891)
