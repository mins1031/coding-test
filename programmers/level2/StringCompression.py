def solution(s):
    answer = 0
    leng = len(s)
    res = [s]
    for i in range(2, (leng // 2) + 1):
        j = i
        tmp_res = ""
        tmp = s[0:j]
        count = 0
        while leng > j:
            if j + i >= leng:
                break
            if s[j:j+i] == tmp:
                count += 1
            else:
                tmp = s[j:j+i]
                if count != 0:
                    tmp_res += str(count) + tmp
                else:
                    tmp_res += tmp
            j += i
        tmp += s[j:-1]
        tmp += s[-1]
        res.append(tmp_res)
        # for j in range(0, len(s), i):
    return answer

st1 = "aabbaccc"
st2 = "ababcdcdababcdcd"
st3 = "abcabcdede"
st4 = "abcabcabcabcdededededede"
st5 = "xababcdcdababcdcd"
print(solution(st1))
"""실패"""