n = int(input())
dolls = sorted(map(int, input().split()))

length = len(dolls)
empty_doll = [True] * length
empty_cnt = length

for i in range(length):
    j = i + 1
    while j < length:
        if dolls[j] > dolls[i] and empty_doll[j]:
            empty_doll[j] = False
            empty_cnt -= 1
            break
        j += 1

print(empty_cnt)
