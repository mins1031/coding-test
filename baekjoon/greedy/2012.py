n = int(input())
wins = [0]

for i in range(n):
    wins.append(int(input()))

wins.sort()
result = 0
for i in range(1, n+1):
    upset_percent = abs(i - wins[i])
    result += upset_percent

print(result)