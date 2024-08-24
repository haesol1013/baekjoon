word = input().upper()
word_list = list(set(word))
word_cnt = []

for i in word_list:
    count = word.count(i)
    word_cnt.append(count)

if word_cnt.count(max(word_cnt)) > 1:
    print('?')
else:
    max_index = word_cnt.index(max(word_cnt))
    print(word_list[max_index])
