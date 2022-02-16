n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

table = {}
for i in range(n):
    key = n_list[i] % n
    table[key] = n_list[i]

for i in m_list:
    key = i % n
    if table[key] == i:
        print(1)
    else:
        print(0)
