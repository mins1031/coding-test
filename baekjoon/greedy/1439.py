n = str(input())

index = 0
zero_count = 0
one_count = 0
present = n[0]
if present == "0":
    zero_count += 1
else:
    one_count += 1

for i in range(1, len(n)):
    if present == n[i]:
        continue
    else:
        if n[i] == "0":
            zero_count += 1
        else:
            one_count += 1
        present = n[i]

if zero_count > one_count:
    print(one_count)
elif one_count > zero_count:
    print(zero_count)
elif (zero_count == 0 and one_count == 1) or (zero_count == 1 and one_count == 0):
    print(1)
elif zero_count == one_count:
    print(zero_count)

