def solution(id_list, report, k):
    answer = []
    reported_dic = dict()
    report_dic = dict()
    for i in id_list:
        reported_dic[i] = []
        report_dic[i] = []

    for i in range(len(report)):
        tmp_list = report[i].split(" ")
        if tmp_list[1] in report_dic[tmp_list[0]]:
            continue
        else:
            report_dic[tmp_list[0]].append(tmp_list[1])
            reported_dic[tmp_list[1]].append(tmp_list[0])

    stop_ids = []
    for i in reported_dic:
        if len(reported_dic[i]) >= k:
            stop_ids.append(i)

    for value in report_dic.values():
        tmp_count = 0
        for i in stop_ids:
            if i in value:
                tmp_count += 1
        answer.append(tmp_count)

    return answer

def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3

print(solution(id_list, report, k))
print(solution(id_list2, report2, k2))
