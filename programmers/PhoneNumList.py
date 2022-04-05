def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) -1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break

    return answer

# 개인적으론 해시를 사용한 아래 풀이가 더 좋은것 같다.
# 이거 시간복잡도 N^2 되면 안되서 이중포문 못써서 못건드렸는데 아래 내용은 첫 for는 1,000,000이지만 두번쨰 for는 번호의 갯수로 돌기 때문에 20이므로 n^2이 되지 않고 o(n)이 된다고 한다.
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

s = ["119", "97674223", "1195524421"]
print(solution(s))
