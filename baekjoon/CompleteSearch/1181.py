n = int(input())
list = []

for i in range(n):
    word = input()
    list.append(word)

result = sorted(list, key = lambda x : len(x), sorted())
print(result)
