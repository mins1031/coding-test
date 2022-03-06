import sys
from collections import deque

sys.stdin = open("in_out/chapter7/in1.txt", "rt")

def bfs(my, song):
    need_visit = deque()
    need_visit.append(my)
    stop = False
    while need_visit:
        now = need_visit.popleft()
        for next in (now+5, now+1, now-1):
            if 0<next<10000:
                need_visit.append(next)
                des[next] = des[now] + 1
                if next == song:
                    stop = True
                    break
        if stop:
            break
    return des[song]

if __name__ == "__main__":
    my, song = map(int, input().split())
    move = [5, 1, -1]
    des = [0] * (10000+1)

    print(bfs(my, song))