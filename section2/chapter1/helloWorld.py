import sys
sys.stdin = open("section2/chapter1/in3.txt", "rt")

def sol(n, k):
    temp_list = list()
    for i in range(1, n + 1):
        if n % i == 0:
            temp_list.append(i)

    if len(temp_list) < k:
        return -1

    return temp_list[k - 1]

n , k = map(int, input().split())
print(sol(n, k))

'''
or
n , k = map(int, input().split())
cnt = 0 
for i in range(1, n + 1):
    if n % i == 0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
    
for -else는 반복문이 정상적으로 다 동작하면 else구문을 실행해준다.
'''
