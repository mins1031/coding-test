
n, p = map(int, input().split()) # n : 연주 음의 총 갯수 , p : 줄당 플랫의 총갯수

stack = [[0], [0], [0], [0], [0], [0], [0]]
cnt = 0
for i in range(n):
    line, plat = map(int, input().split())  # line : 몇번 줄인지 , plat : 줄의 몇번 플랫 인지
    stack_leng = len(stack[line])
    while stack[line][-1] > plat:
        stack[line].pop()
        cnt += 1

    if stack[line][-1] == plat:
        continue

    stack[line].append(plat)
    cnt += 1

print(cnt)
# 문제'풀이'에 집중하지 말고 문제 '해결'에 집중하자.