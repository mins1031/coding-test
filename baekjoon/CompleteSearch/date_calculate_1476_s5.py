e, s, m = map(int, input().split())

e_value = 1
s_value = 1
m_value = 1
year = 1

while True:
    if e_value == e and s_value == s and m_value == m:
        break

    if e_value == 15:
        e_value = 1
    else:
        e_value += 1

    if s_value == 28:
        s_value = 1
    else:
        s_value += 1

    if m_value == 19:
        m_value = 1
    else:
        m_value += 1


    year += 1

print(year)
