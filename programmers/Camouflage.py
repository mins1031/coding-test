def solution(clothes):
    answer = 0
    for i in range(len(clothes)):
        answer += 1
        for j in range(i, len(clothes)):
            tmp = 1
            if clothes[j][1] == clothes[i][1]:
                continue
            answer += tmp
            tmp += 1

    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["dd","aa"], ["green_turban", "headgear"]]
clothes2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
# 실패! 유사Dp임