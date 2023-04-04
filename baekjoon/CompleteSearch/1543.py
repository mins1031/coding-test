document = input()
word = input()

document_length = len(document)
word_length = len(word)

check_document = [0 for _ in range(document_length)]
result = 0

for i in range(document_length - (word_length - 1)):
    if document[i] == word[0]:
        document_index = i
        for j in range(word_length):
            if document[document_index] != word[j] or check_document[document_index] != 0:
                break
            elif document[document_index] == word[j] and check_document[document_index] == 0:
                check_document[document_index] = 1
                document_index += 1
        else:
            result += 1

print(result)
