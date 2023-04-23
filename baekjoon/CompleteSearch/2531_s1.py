n, d, k, c = map(int, input().split())
pieces = []
for _ in range(n):
    pieces.append(int(input()))

link_index_pieces = pieces[:k-1]
pieces.extend(link_index_pieces)

max_value = 0

for i in range(n):
    temp_pieces = pieces[i:i+k]
    temp_max = 0
    temp_pieces = set(temp_pieces)
    if c not in temp_pieces:
        temp_max += 1
    temp_max += len(temp_pieces)

    if temp_max > max_value:
        max_value = temp_max

print(max_value)
