"""""""""
# 세 막대
"""""""""

arr = list(map(int, input().split()))
arr.sort()
max_side = arr.pop()
extra_side = sum(arr)

while not (max_side < extra_side):
    max_side -= 1

result = max_side + extra_side
print(result)
