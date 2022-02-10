doc = str(input())
word = str(input())

count = 0
check_cnt = 0
index = 0

for i in range(doc):
    if doc[i] == word[0]:
        temp_word = doc[index: index + 3]
    if word == temp_word:
        check_cnt += 1

print(check_cnt)

