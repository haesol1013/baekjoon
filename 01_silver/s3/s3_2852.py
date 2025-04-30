# NBA 농구 - 2852

def time_to_sec(time_str: str) -> int:
    m, s = map(int, time_str.split(':'))
    return m*60 + s


def sec_to_time(sec: int) -> str:
    return f"{sec // 60:02d}:{sec % 60:02d}"


def update_lead_time(score: list[int], lead_time: list[int], duration: int):
    if score[0] > score[1]:
        lead_time[0] += duration
    elif score[1] > score[0]:
        lead_time[1] += duration


n = int(input())
score = [0, 0]
lead_time = [0, 0]
prev_time = 0

for _ in range(n):
    team_str, time_str = input().split()
    curr_time = time_to_sec(time_str)

    update_lead_time(score, lead_time, curr_time - prev_time)

    score[int(team_str)-1] += 1
    prev_time = curr_time

update_lead_time(score, lead_time, time_to_sec("48:00")-prev_time)

print(sec_to_time(lead_time[0]))
print(sec_to_time(lead_time[1]))
