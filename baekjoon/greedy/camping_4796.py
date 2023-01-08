
case_count = 1
result = []
while (True) :
    l, p, v = input().split(" ")
    if l == "0" and p == "0" and v == "0" :
        break

    pull_days_count = int(v) // int(p)
    rest_days = int(v) % int(p)

    if rest_days > int(l) :
        rest_days = int(l)

    result_days = (pull_days_count * int(l)) + rest_days

    result.append("Case " + str(case_count) + ": " + str(result_days))
    case_count += 1

for i in result :
    print(i)
