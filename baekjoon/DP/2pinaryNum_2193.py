n = int(input())
data = [1,1,2]

for i in range(3,91):
    data.append(data[i-1]+data[i-2])

print(data[n-1])