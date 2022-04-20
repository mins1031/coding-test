def solution(prices):
    answer = []
    leng = len(prices)
    for i in range(0, leng):
        time = 0
        for j in range(i+1, leng):
            time += 1
            if prices[i] > prices[j]:
                break
        answer.append(time)

    return answer


price = [1, 2, 3, 2, 3]
print(solution(price))
