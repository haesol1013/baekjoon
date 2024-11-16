# Pectopah - 23738

dict_ = {
    "B": "v",
    "E": "ye",
    "H": "n",
    "P": "r",
    "C": "s",
    "Y": "u",
    "X": "h"
}

word = input()

for s in word:
    if s in dict_:
        print(dict_[s], end="")
    else:
        print(s.lower(), end="")
