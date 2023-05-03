def end_loop():
    global temp_n
    find_b = False
    end_message = True
    for i in range(len(temp_n)):
        if not find_b and temp_n[i] == 'b':
            find_b = True
        if find_b and temp_n[i] == 'a':
            end_message = False

    return end_message

n = list(str(input()))

start_b_index = 0
end_b_index = 0
n_length = len(n)
b_count = 0
for i in range(n_length):
   if n[i] == 'b':
       start_b_index = i
       break
for i in range(n_length -1, -1, -1):
   if n[i] == 'b':
       end_b_index = i + 1
       break

for i in range(n_length):
    if n[i] == 'b':
        b_count += 1

temp_n = n[start_b_index:end_b_index:1]

count = 0
result = 0

while True:
    if count == len(temp_n):
        break

    if end_loop():
        break

    if temp_n[count] == 'b':
        for i in range(len(temp_n) -1, -1, -1):
            if temp_n[i] == 'a':
                temp_n[count], temp_n[i] = 'a', 'b'
                result += 1
                break
    count += 1
print(result)

