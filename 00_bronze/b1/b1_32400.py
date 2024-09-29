# 다트판 - 32400

arr = list(map(int, input().split()))
idx = arr.index(20)
expect = 20 + arr[(idx+1)%20] + arr[idx-1]
if expect/3 > 10.5:
    print("Alice")
elif expect/3 < 10.5:
    print("Bob")
else:
    print("Tie")
