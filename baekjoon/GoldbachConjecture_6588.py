from sys import stdin

array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    n = int(stdin.readline())

    if n == 0: break

    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(n, "=", i, "+", n-i)
            break

'''소수를 구하는 과정을 도출하는건 정말 쉬웠는데 그다음 b-a가 어렵고 풀이를 봐도 잘 모르겠다. 어쨰서 if array[i] and array[n-i]: 이부분이 n이 되는지를 모르겠다;;
'''




