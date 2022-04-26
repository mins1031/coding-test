def solution(dartResult):
    plus_score = {"S": 1, "D": 2, "T": 3}
    reword = {"*": 2, "#": -1}
    tmp = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if i != 0 and dartResult[i] == "0" and dartResult[i - 1] == "1":
                tmp[-1] = 10
                continue
            tmp.append(int(dartResult[i]))
            continue
        elif dartResult[i] in plus_score:
            tmp[-1] = tmp[-1] ** plus_score.get(dartResult[i])
            continue
        else:
            if dartResult[i] == "*":
                if len(tmp) <= 1:
                    tmp.append("*")
                else:
                    if tmp[-2] in reword:
                        tmp[-2] += "*"
                    else:
                        tmp.insert(-1, "*")
                    tmp.append("*")
            else:
                if tmp[-1] == "*":
                    tmp[-1] += "#"
                else:
                    tmp.append("#")
    res = []
    for i in tmp:
        if str(i).isdigit():
            res.append(i)
        else:
            middle = 1
            for j in i:
                middle *= reword.get(j)

            res[-1] *= middle

    return sum(res)


dartResult = "1S2D*3T"
dartResult2 = "1D2S#10S"
dartResult3 = "1D2S0T"
dartResult4 = "1S*2T*3S"
dartResult5 = "1D#2S*3S"
dartResult6 = "1T2D3D#"
dartResult7 = "1D2S3T*"
print(solution(dartResult))
print(solution(dartResult2))
print(solution(dartResult3))
print(solution(dartResult4))
print(solution(dartResult5))
print(solution(dartResult6))
print(solution(dartResult7))

'''
1. 일단 점수 기록하는 리스트도 하나 있어야 할듯.
2. dartResult를 돌며 숫자가 나오면 리스트에 넣고 문자나 특수문자가 나오면 리스트의 마지막 값에 적용하는 식으로 구현해야 ㅎ할듯.
'''
