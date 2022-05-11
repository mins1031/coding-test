import math


def solution(str1, str2):
    tmp_str1 = ""
    tmp_str2 = ""
    for i in str1:
        if not i.isalpha():
            tmp_str1 += i
            continue
        tmp_str1 += i.lower()

    for i in str2:
        if not i.isalpha():
            tmp_str2 += i
            continue
        tmp_str2 += i.lower()

    two_words = []
    for i in range(len(tmp_str1)-1):
        element = tmp_str1[i:i + 2]
        if not element.isalpha():
            continue
        two_words.append(element)
    for i in range(len(tmp_str2)-1):
        element = tmp_str2[i:i + 2]
        if not element.isalpha():
            continue
        two_words.append(element)

    not_common = set(two_words)
    tmp_common = {}
    common = 0
    for i in two_words:
        try:
            tmp_common[i] += 1
        except:
            tmp_common[i] = 1

    for i in tmp_common.values():
        if i > 1:
            common += 1

    jacad_share = len(not_common)
    jacad_rest = common
    answer = math.trunc((jacad_rest / jacad_share) * 65536)
    return answer

l1 = ["l","a","b"]
l2 = ["b","c","z","a"]

str1 = "FRANCE"
str2 = "french"
print(solution(str1, str2))
''
str1 = "handshake"
str2 = "shake hands"
# print(solution(str1, str2))

str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1, str2))

str1 = "E=M*C^2"
str2 = "e=m*c^2"
# print(solution(str1, str2))

