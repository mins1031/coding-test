def solution(n):
    n_two = list(str(bin(n)[2:]))
    n_cnt = 0
    for i in n_two:
        if i == "1":
            n_cnt += 1

    tmp = n
    answer = 0
    while True:
        tmp += 1
        temp_two = list(str(bin(tmp)[2:]))
        tmp_cnt = 0
        for i in temp_two:
            if i == "1":
                tmp_cnt += 1

        if n_cnt == tmp_cnt:
            answer = tmp
            break
    return answer

def solution2(n):
    n_two = bin(n)
    n_cnt = n_two.count('1')
    tmp = n
    answer = 0
    while True:
        tmp += 1
        tmp_cnt = bin(tmp).count('1')
        if n_cnt == tmp_cnt:
            answer = tmp
            break
    return answer



n = 78
n2 = 15

print(solution2(n))