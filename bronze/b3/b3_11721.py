"""""""""
# 10개 씩 끊어 출력하기
"""""""""

str_ = input()
while len(str_) > 10:
    sub_str = str_[:10]
    str_ = str_[10:]
    print(sub_str)
print(str_)