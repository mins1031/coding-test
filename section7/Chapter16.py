import sys


# sys.stdin = open("in_out/chapter15/in1.txt", "rt")



if __name__ == "__main__":
    n, m = map(int, input().split())
    tomatos = [list(map(int, input().split())) for _ in range(m)]
    ch = [[0] * n for _ in range(m)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]