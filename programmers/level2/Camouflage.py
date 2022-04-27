from itertools import combinations
def solution(clothes):
    answer = 0
    leng = len(clothes)
    for i in range(1, leng+1):
        tmp = list(combinations(clothes, i))
        if i != 1:
            for j in tmp:
                print(j)
                print(j[0][1])
                print(j[1][1])


    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))
# 실패! 유사Dp임