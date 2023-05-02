n, m = map(int, input().split())
s = set()
m_list = set()

for i in range(n):
    temp_n = str(input())
    s.add(temp_n)

result = 0
for i in range(m):
    temp_m = str(input())
    if temp_m in s:
        result += 1
print(result)

# result = m_list.intersection(s)

# print(len(result))



# TODo 두번째 시도 - 첫 알파의 아스키코드 - 97를 해시테이블의 인덱스 처럼 활용해 풀었으나 역시 시간초과
# for i in range(m):
#     compare_word = m_list[i]
#     compare_word_index = contract_alpha_index(compare_word[0])
#     if compare_word in s[compare_word_index]:
#         result += 1
#
# print(result)

# TODO 첫 시도 - 첫 알파벳으로 비교해 자신보다 같으면 연산 수행. 자기보다 크면 다음 m으로 넘어감 -> 초반에는 빠르지만 뒤로갈수록 n^2에 수렴해감. 결국 최악엔 한 알파에 1만개 단어가 정의되어있으면 그냥. 소용없음.
# s_head_ascii_list = []
# s_head_ascii_list.sort()
# for i in range(m):
#     compare_word = m_list[i]
#     compare_word_head_ascii = ord(compare_word[0])
#     for j in range(n):
#         if compare_word_head_ascii == s_head_ascii_list[j]:
#             if compare_word == s[j]:
#                 result += 1
#         elif compare_word_head_ascii < s_head_ascii_list[j]:
#             break
# print(result)
