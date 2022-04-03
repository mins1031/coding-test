from itertools import permutations

n = int(input())
array = []

for i in range(1, n+1):
    array.append(i)

result = list(permutations(array, n))

for i in result:
    for j in i:
        print(j, end=' ')
    print()


'''
-> bfs 풀이
n = int(input())
temp = []

def dfs():
    if len(temp) == n:
        print(*temp)
        return
    for i in range(1, n + 1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()

dfs()
'''

