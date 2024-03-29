import sys


def cnt(assign):
    score_list = []
    score = 0

    for i in assign:
        if i == 'O':
            score += 1
            score_list.append(score)
        else:
            score = 0
            score_list.append(score)

    return sum(score_list)


T = int(input())

for i in range(T):
    quiz_result = sys.stdin.readline()
    sum_score = cnt(quiz_result)
    print(sum_score)
