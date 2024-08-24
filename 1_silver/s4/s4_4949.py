# 균형잡힌 세상 - 4949

import sys
input = lambda: sys.stdin.readline().rstrip()


def is_balanced(sentence: str) -> str:
    stack = []
    for char in sentence:
        match char:
            case "(" | "[":
                stack.append(char)
            case ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(char)
            case "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(char)
            case _:
                continue
    return "no" if stack else "yes"


def main():
    while True:
        str_ = input()
        if str_ == ".":
            break
        print(is_balanced(str_))


main()
