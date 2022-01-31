import sys

sys.stdin = open("in_out/chapter4/in1.txt", "rt")


def sol(n, m, list1, list2):
    # 이거는 nlog n의 복잡도를 가지는 풀이
    # list1.extend(list2)
    # list1.sort()

    # 두개의 리스트를 두개의 임의 인덱스를 설정해 대소비교를 해준다.
    # 각 인덱스 값끼리 비교하며 작은것을 결과 리스트에 추가해준다.
    # 비교하다 한쪽 인덱스가 헤당 리스트의 길이보다 커지면 그 리스트이 마지막수가 현재까지 두 리스트에서 거쳐간 인덱스의 값중 제일 큰값이기 때문에 인덱스가 남은 리스트의 남은 내용들을 결과 리스트에 붙혀준다.
    # 이게 시간복잡도 n의 풀이이다.
    p1, p2 = 0, 0
    res = list()
    while n > p1 and m > p2:
        if list1[p1] <= list2[p2]:
            res.append(list1[p1])
            p1 += 1
        else:
            res.append(list2[p2])
            p2 += 1

    if n > p1:
        res = res + list1[p1:]
    if m > p2:
        res = res + list2[p2:]

    return res


n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))
result = sol(n, m, n_list, m_list)
for i in result:
    print(i, end=' ')
