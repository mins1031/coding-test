import sys

sys.stdin = open("in_out/chapter1/in5.txt", "rt")


# 우선 내가한 방식은 반복문 돌며 해당 문자열을 회문으로 만들어 원본과 회문의 글자 하나하나를 비교하는 방식으로 구현했다.
def sol(n, n_list):
    res = ["" for _ in range(n)]

    for i in range(n):
        reverse_letter = "".join(reversed(n_list[i]))
        tmp = n_list[i]
        for j in range(len(tmp)):
            if tmp[j].lower() != reverse_letter[j].lower():
                res[i] = "NO"
                break
        else:
            res[i] = "YES"

    return res


n = int(input())
str_list = list()

for i in range(n):
    str_list.append(str(input()))

same_candy_max_count = sol(n, str_list)

for i in same_candy_max_count:
    print(i)
# ============ 강의 코드 ===============
# size //2 를 해주는 이유는 조건문의 조건에 있다. s[j] != s[-1 - j] 형태는 j가 0 일때 (0과 5를) 1일때 (1과 4를) .... 이렇게 돌기 때문에 결국 중간값보다 하나 작은 수까지만 구하면 된다.
result2 = ["" for _ in range(n)]
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1 - j]:
            print("#%d NO" % (i + 1))
            break
    else:
        print("#%d YES" % (i + 1))

# 또한 더 쉬운 방법이 있는데 s2[::-1]는 리스트 자체를 회전시켜준다. 즉 s2와 s2[::-1]이 같은지만 확인해 주면 문자열 역전은 끝나게 된다. 하지만 왠만하면 위의 내용이 좋다.
for i in range(n):
    s2 = input()
    s2 = s2.upper()
    print(s2[::-1])
    if s2==s2[::-1]:
        print("#%d NO" % (i + 1))
    else:
        print("#%d YES" % (i + 1))