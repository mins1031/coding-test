def solution(p):
    present = 0
    array_leng = len(p)
    change_count = [0] * array_leng

    for i in range(array_leng):
        stand = min(p[i:array_leng])
        stand_index = p.index(stand)
        if stand_index != present:
            p[present], p[stand_index] = p[stand_index], p[present]
            change_count[present] += 1
            change_count[stand_index] += 1
        present += 1
    return change_count

p = [2,5,3,1,4]
print(solution(p))