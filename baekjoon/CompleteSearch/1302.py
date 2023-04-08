n = int(input())
titles = []

for i in range(n):
    book_title = str(input())
    titles.append(book_title)

distinct_title = sorted(list(set(titles)))
biggest_title_count = 0
result = ""
index = 0
titles.sort()

for i in distinct_title:
    temp_max_count = 0
    for j in range(len(titles)):
        match = False
        if titles[j] == i:
            match = True
            temp_max_count += 1

        if match and titles[j] != i:
            break

    if temp_max_count > biggest_title_count:
        biggest_title_count = temp_max_count
        result = i

print(result)






