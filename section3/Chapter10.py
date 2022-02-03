import sys

sys.stdin = open("in_out/chapter10/in1.txt", "rt")

doku = [list(map(int, input().split())) for _ in range(9)]
check = list()

