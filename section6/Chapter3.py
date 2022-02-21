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

