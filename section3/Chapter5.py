import sys

sys.stdin = open("in_out/chapter5/in5.txt", "rt")


def sol(n, m, n_list):
    # for i in range(n):
    #     tmp_sum = n_list[i]
    #     for j in range(i+1, n):
    #         tmp_sum += n_list[j]
    #         if tmp_sum == m:
    #             res += 1
    #             break
    #         elif tmp_sum > m:
    #             break
    # 이중포문 이제 부터 지양하면서 구현해보자
    res = 0
    lt = 0
    rt = 1
    total = n_list[0]

    while True:
        if total < m:
            if rt < n:
                total += n_list[rt]
                rt += 1
            else:
                break
        elif total == m:
            res += 1
            total -= n_list[lt]
            lt += 1
        else:
            total -= n_list[lt]
            lt += 1

    return res


n, m = map(int, input().split())
n_list = list(map(int, input().split()))

print(sol(n, m, n_list))

'''
설명: 이중포문으로 하려했으나 속도면에서 너무 안좋음 그래서 무한루프 도는 while문과 수동으로 인덱스 이동시키는 로직을 통해 구현함
원리는 우선 시작 인덱스부터 1씩 인덱스를 증가하며 해당 값들을 더해 m이 얼마나 나오는지를 카운트 해야되는 문제이다 
해서 total(더한값)을 기준으로 각각 현재 total이 m보다 큰지 같은지 작은지를 판단해 해당 사항에 맞는 로직을 구현한다
1. 우선 total이 m보다 작은경우 total에 리스트[rt(이동값)]값을 중첩덧셈 하고 rt값을 1증가시킨다 
2. total이 m과 같은 경우 cnt(카운트)를 1증가 시키고 total에 리스트[lt(기준값)]를 뺴준다. 이후 lt를 1증가시키고 종료한다
3. 왜 total에 리스트[lt(기준값)]를 뺴주는가? -> 처음엔 total이 m보다 작아 계속 rt값이 증가한다. 그러다 m과 같거나 더 큰 상황이 오면 lt부터 시작한 합은 m인지 아닌지에 대한 계산은 끝났기 때문에 lt를 다음수로
넘겨야 한다. 이제 여기서 total에 기존 lt값을 빼게 되면 자연스럽게 다음 lt값의 동등여부를 확인할수 있다 물론 동등여부를 확인할 수 없는 경우도 있지만 rt값이 증가함에 따라 달라질 이야기다.
'''