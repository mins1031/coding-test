import sys

sys.stdin = open("in_out/chapter7/in1.txt", "rt")



if __name__ == "__main__":
    my, song = map(int, input().split())
    move = [5, 1, -1]
    dfs(0, my, 0)