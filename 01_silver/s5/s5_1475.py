# 방 번호 - 1475

room_num = list(map(int, input()))
num_cnt = [0] * 10
for i in room_num:
    num_cnt[i] += 1

num_cnt[6], num_cnt[9] = (num_cnt[6]+num_cnt[9]), 0
while num_cnt[6] > num_cnt[9]:
    num_cnt[6] -= 1
    num_cnt[9] += 1

print(max(num_cnt))
