e, s, m = map(int, input().split())

e_max = 15
s_max = 28
m_max = 19

year = 1
while True:
    if e == e_max and s == s_max and m == m_max:
        year = 7980
        break

    temp_e = year % e_max
    temp_s = year % s_max
    temp_m = year % m_max

    if temp_e == e and temp_s == s and temp_m == m:
        break

    year += 1

print(year)
