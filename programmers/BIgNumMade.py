def solution(number, k):
    answer = []

    for num in number:
        if not answer:
            answer.append(num)
            continue
        while answer[-1] < num:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(num)

    return answer

s1 = "1924"
k1 = 2
s2 = "1231234"
k2 = 3
s3 = "4177252841"
k3 = 4

print(solution(s1, k1))
print(solution(s2, k2))
print(solution(s3, k3))
