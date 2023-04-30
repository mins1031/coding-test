n = int(input())
size_index_list = [[] for _ in range(51)]

for i in range(n):
    word = str(input())
    word_size = len(word)
    size_index_list[word_size].append(word)

for i in range(1, 51):
    if len(size_index_list[i]) == 0 :
        continue

    size_index_list[i] = list(set(size_index_list[i]))
    size_index_list[i].sort()

for i in range(1, 51):
    same_size_word_count = len(size_index_list[i])
    if same_size_word_count == 0 :
        continue

    for j in range(same_size_word_count):
        print(size_index_list[i][j])

