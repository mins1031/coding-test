def solution(record):
    answer = []
    users = dict()
    for i in record:
        tmp = list(i.split(' '))
        if tmp[0] == "Enter":
            answer.append(tmp[1])
            answer.append("님이 들어왔습니다.")
            users[tmp[1]] = tmp[2]
        elif tmp[0] == "Leave":
            answer.append(tmp[1])
            answer.append("님이 나갔습니다.")
        else:
            users[tmp[1]] = tmp[2]
    res = []
    for i in range(0, len(answer), 2):
        if answer[i] in users.keys():
            res.append(users[answer[i]] + answer[i+1])

    return res


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
