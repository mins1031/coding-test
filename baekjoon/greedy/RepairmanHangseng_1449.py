import sys

n, tape = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()

pipe = [0 for _ in range(max(array) + 1)]

cnt = 0
for i in range(n):
    if pipe[array[i]] == 1:
        continue
    else:
        if array[i] + tape > len(pipe):
            cnt += 1
            continue
        for j in range(tape):
            pipe[array[i] + j] = 1
        cnt += 1

print(cnt)

# TODO 값은 다 나오는데 잘 나오는데 채점은 안됨. 시간 초과도 아니고 틀림.