def solution(number, k):
    answer = [number[0]]
    cnt = 0
    for i in range(1, len(number)):
        if cnt == k:
            answer.extend(number[i:])
            break
        if number[i - 1] < number[i]:
            while True:
                if not answer or cnt == k :
                    break
                if cnt != k and number[i] > answer[-1]:
                    answer.pop()
                    cnt += 1
                    continue
                else:
                    break
            answer.append(number[i])
        else:
            answer.append(number[i])

    if cnt == 0:
        for i in range(k):
            answer.pop()

    return "".join(answer)


s1 = "1924"
k1 = 2
s2 = "1231234"
k2 = 3
s3 = "4177252841"
k3 = 4

plus1 = "654321"
pk1= 1
plus2 = "654321"
pk2= 5

# print(solution(s1, k1))
# print(solution(s2, k2))
# print(solution(s3, k3))
print(solution(plus1, pk1))
print(solution(plus2, pk2))
