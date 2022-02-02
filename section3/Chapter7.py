import sys


sys.stdin = open("in_out/chapter7/in1.txt", "rt")

def sol(n, apple_trees):
    standard = n // 2
    result = 0
    # lt = 0
    # rt = 0
    # for i in range(standard+1):
    #     lt = standard - i
    #     rt = standard + i
    #     result += sum(apple_trees[i][lt:rt+1])
    #
    # reverse_standard = n - 1
    # for i in range(standard):
    #     lt = standard - i
    #     rt = standard + i
    #     result += sum(apple_trees[reverse_standard][lt:rt + 1])
    #     reverse_standard -= 1

    s=e=standard
    for i in range(n):
        result += sum(apple_trees[i][s:e + 1])
        if i >= standard:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1


    return result


n = int(input())
apple_trees = [list(map(int, input().split())) for _ in range(n)]

print(sol(n, apple_trees))
