'''
d(n)은 n + n의 자릿수들 임. ex -> d(35) = 35 + 3 + 5 = 43
d(n)은 무한수열이 가능 d(n), d(d(n)), d(d(d(n)))...
n은 d(n)의 생성자라고 함. ex -> 35는 43의 생성자중 하나.
생성자는 여러개가 가능
생성자가 없는 수도 있음. 이수를 '셀프넘버' 라고 한다
10000이하에서 셀프넘버들을을구하라

-> answer
1. 1부터 10000까지 d(n)값을 만들어 리스트에 넣고 중복제거 
2. 이후 또 1부터 10000까지 포문돌며 없는것들 출력해주면 될듯.
가만히 생각할땐 안보였는데 뭔가 쓰면서 하니 생각이 났다. 가만히 생각 보단 끄적끄적 해보자.
'''

not_self_nums = [2, 4, 6, 8, 10, 11, 12] # 셀프넘버가 아닌 수들의 리스트

for i in range(1, 10000): # 1부터 1   만 까지 i를 생성자로 생성하는 수를 만들어 리스트에 추가.
    be_split_num = list(map(int, str(i))) # i를 자릿수별로 나눔.
    if len(be_split_num) == 1 : # i가 1자리수인경우
        not_self_num = i + be_split_num[0] # 기존 수 더하기 자릿수들
        not_self_nums.append(not_self_num) # 셀프넘버 아닌 리스트에 추가.
    elif len(be_split_num) == 2 : # i가 2자리수인경우
        not_self_num = i + be_split_num[0] + be_split_num[1]
        not_self_nums.append(not_self_num)
    elif len(be_split_num) == 3 : # i가 3자리수인경우
        not_self_num = i + be_split_num[0] + be_split_num[1] + be_split_num[2]
        not_self_nums.append(not_self_num)
    elif len(be_split_num) == 4 : # i가 4자리수인경우
        not_self_num = i + be_split_num[0] + be_split_num[1] + be_split_num[2] + be_split_num[3]
        not_self_nums.append(not_self_num)

for i in range(1, 10000) :
    if i not in not_self_nums: # 1~1만까지 돌며 i가 셀프넘버에 없는 수면 셀프넘버이므로 출력.
        print(i)
