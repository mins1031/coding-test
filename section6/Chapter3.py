import sys

sys.stdin = open("in_out/chapter3/in2.txt", "rt")

def sol(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=" ")
        print()
    else:
        ch[v] = 1
        sol(v+1)
        ch[v] = 0
        sol(v+1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1);
    sol(1)

'''
모든 부분집합들을 구하는 문제
단순하게 n까지의 정수들로 트리를 만들어 트리를 돌며 해당 값을 사용할지 말지에 대한 분기로 하나의 집합을 만들어가며
L==n이 될때까지 돌다 해당 조건이 되면 집합을 출력하고 리턴하며 반복하는데 이떄 집합이기에 중복수가 있어선 안되어 중복방지용인 리스트를 통해 중복을 방지한다.
'''

