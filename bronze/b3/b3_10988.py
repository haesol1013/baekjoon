word = input()
reversed_word = ''.join(reversed(word))

if word == reversed_word:
    print(1)
else:
    print(0)