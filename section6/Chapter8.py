import sys


sys.stdin = open("in_out/chapter8/in5.txt", "rt")

def dfs(L):
    global res, count
    if L == m:
        if len(res) != len(set(res)):
            return
        for i in res:
            print(i, end=' ')
        print()
        count += 1
        return
    else:
        for i in marbles:
            res[L] = i
            dfs(L+1)
# def dfs(L):
#     global res, count
#     if L == m:
#         for i in res:
#             print(i, end=' ')
#         print()
#         count += 1
#     else:
#         for i in range(1, n+1):
#             if ch[i] == 0:
#                 ch[i] = 1
#                 res[L] = i
#                 dfs(L+1)
#                 ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    marbles = list()
    for i in range(1, n+1):
        marbles.append(i)
    res = [0] * m
    count = 0
    dfs(0)
    print(count)

'''
6번 문제와 유사한데 차이점은 중복을 방지해야 한다는 점이었다. 중복 방지가 조금 까다로웠는데 간단하게 생각해서 그냥 중복인경우 배제해주면 되는 것이었다.
우선 나는 레벨이 다 채워진후 추가해온 배열의 길이와 set한 길이를 비교해 다르면 중복이 있는 것이므로 해당 경우를 배제하는 방식으로 구현했고
강의에서는 체크리스트를 하나 만들어 현제 결과 배열에 추가된 값은 체크리스트의 추가된값의 인덱스에 1을 넣어줌으로써 중복을 확인해 배제하는 방식으로 구현했다. 
일반적으로 체크리스트를 사용하는 방법이 속도면에서 유리하다고 판단되어 앞으로 이런 중복을 체크해야 하는 경우 체크리스트를 사용해야겠다
'''