import sys

sys.stdin = open("in_out/chapter3/in5.txt", "rt")


def sol(a, b, target):
    depth = b - a + 1
    for i in range(depth // 2):
        # temp = target[a + i]
        # target[a + i] = target[b - i]
        # target[b - i] = temp
        # 파이썬은 swap이라는 기능을 통해 위처럼 하지 않아도 바로 바꿔줄수 있다
        target[a + i], target[b - i] = target[b - i], target[a + i]


target = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    sol(a - 1, b - 1, target)

for i in range(len(target)):
    print(target[i], end=' ')
