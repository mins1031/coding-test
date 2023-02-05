
'''
while로 돌면서 2글자 아님 3글자니 입력받은 문자열을 2개로 나누어서 알파에 있는지 확인하고 있으면 카운팅 없으면 계속진행하다 3글자로 변경. 이런식으로 진행.
'''
def input_str_spliter_two(n, input_length):
    split_two = []
    for i in range(input_length):
        if i == input_length - 1:
            split_two.append(n[i])
        else:
            split_two.append(n[i] + n[i + 1])
    return split_two

def input_str_spliter_three(n, input_length):
    split_three = []
    for i in range(input_length):
        if i == input_length - 2:
            split_three.append(n[i] + n[i + 1])
        elif i == input_length - 1:
            split_three.append(n[i])
        else:
            split_three.append(n[i] + n[i + 1] + n[i + 2])
    return split_three

alphas = ["c=","c-","dz=","d-","lj","nj","s=","z="]

n = input()
result = 0
input_length = len(n)
split_two = input_str_spliter_two(n, input_length)
split_three = input_str_spliter_three(n, input_length)

for i in range(len(split_two)) :
    if split_two[i] in alphas:
        result += 1

if "dz=" in split_three:
    result += 1

print(result)