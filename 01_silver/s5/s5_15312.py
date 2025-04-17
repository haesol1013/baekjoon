# 이름 궁합 - 15312

_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_STROKE_LIST = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
STROKE_MAP = dict(zip(_ALPHABETS, _STROKE_LIST))


def get_strokes_for_chars(name: list[str]) -> list[int]:
    return [STROKE_MAP[c] for c in name]


def get_gunghap(stroke_arr: list[int]) -> str:
    curr_arr = stroke_arr[:]
    while len(curr_arr) > 2:
        next_arr = [
            (curr_arr[i]+curr_arr[i+1]) % 10
            for i in range(len(curr_arr)-1)
        ]
        curr_arr = next_arr
    return f"{curr_arr[0]}{curr_arr[1]}"


name1 = input()
name2 = input()
crossed_name_arr = [char for pair in zip(name1, name2) for char in pair]
stroke_arr = get_strokes_for_chars(crossed_name_arr)
result = get_gunghap(stroke_arr)
print(result)
