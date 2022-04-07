n = int(input())
res = 0
tmp = 1
count = 0
while True:
    if n == 0:
        print(count)
        break
    elif n < 0 :
        print(count - 1)
        break
    n -= tmp
    tmp += 1
    count += 1


# for i in range(1, n):
#     tmp += i
#     if tmp > n:
#         res = i - 1
#         break
#     elif tmp == n :
#         res = i
#         break


'''
문제풀이 구상중 제일 처음했던 방법으로 풀었는데 사실 이해가 안된다. 
'''
