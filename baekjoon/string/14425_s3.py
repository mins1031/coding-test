n, m = map(int, input().split())
s = []
s_head_ascii_list = []
m_list = []
for i in range(n):
    temp_n = str(input())
    s.append(temp_n)
    s_head_ascii_list.append(ord(temp_n[0]))

for i in range(m):
    temp_m = str(input())
    m_list.append(temp_m)

set(m_list)

s.sort()
s_head_ascii_list.sort()
m_list.sort()

result = 0
for i in range(m):
    compare_word = m_list[i]
    compare_word_head_ascii = ord(compare_word[0])
    for j in range(n):
        if compare_word_head_ascii == s_head_ascii_list[j]:
            if compare_word == s[j]:
                result += 1
        elif compare_word_head_ascii < s_head_ascii_list[j]:
            break
print(result)

