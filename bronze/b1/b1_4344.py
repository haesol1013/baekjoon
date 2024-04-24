"""""""""
# 평균은 넘겠지
"""""""""

n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    std = sum(arr[1:]) / arr[0]
    ratio = len([score for score in arr[1:] if score > std]) / len(arr[1:]) * 100
    print(f"{ratio:.3f}%")
