import sys

sys.stdin = open("in_out/chapter6/in1.txt", "rt")

def dfs(L, sum):
    global res
    if L == n:
        print(sum)
        res += 1
    else:
        for i in range(len(alpha)):
            if i < 10:
                if password[L] == i:
                    dfs(L+1, sum+alpha[i])
            # else:
'''
실패 dfs 실력 쌓고 다시 풀것.
'''



if __name__ == "__main__":
    n = input()
    password = list()
    alpha = [0, "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
    for i in n:
        password.append(int(i))
    res = 0
    dfs(0, "")
    print(res)
