from itertools import permutations
from collections import deque
def solution(k, dungeons):
    permutation = list(permutations(dungeons, len(dungeons)))
    bigger = 0
    for dun in permutation:
        tmp_bigger = 0
        tmp_k = k
        for x, y in dun:
            if tmp_k <= 0:
                break
            if x <= k :
                tmp_k -= y
                tmp_bigger += 1
        if bigger < tmp_bigger:
            bigger = tmp_bigger

    return bigger

def dfs(L, start, k):
    if L == len(dungeons):
        return
    else:
        for i in range(coin_value[L]+1):
            dfs(L+1, sum+(coins[L] * i))

# 못함 dfs 다시봐야할듯... 일단 풀이 볼것.
k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))

k2 = 40
dungeons2 = [[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]
# answer = 4

print(solution(k2, dungeons2))
