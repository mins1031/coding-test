def solution(n, lost, reserve):
    # 둘의 공통 분모를 제거한 lost 값만이 남는다
    set_lost = set(lost) - set(reserve)
    # 둘의 공통 분모를 제거한 reserve 값만이 남는다
    set_reserve = set(reserve) - set(lost)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    return n - len(set_lost)

lost = [2,4,5,6]
reserve = [1,3,5,6,7]
reserve2 = [3]
n = 10


print(solution(n, lost, reserve))