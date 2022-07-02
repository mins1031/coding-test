def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = set(answer)
    return sorted(list(answer))


numbers = [2, 1, 3, 4, 1]
print(solution(numbers))

numbers = [5,0,2,7]
print(solution(numbers))
