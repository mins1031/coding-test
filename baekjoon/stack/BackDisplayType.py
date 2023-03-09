'''
1. 특수문자용 스택과 알파벳용 리스트를 가진다.
2. 주어진 문자를 돌며 특수문자와 알파벳을 알맞게 저장한다
3. ")"를 찾게되면 알파벳 리스트를 결과 문자열로 더하고 스택의 모든내용이 pop될때 까지 pop하며 문자에 더한다.
4. 이 내용을 반복
5. 문자를 다돌고 남은 내용도 알파벳 문자열에 더하고 스택도 비워서 문자열에 더한다.
'''

stack = []
alpha = []
result_string = ""

types = ["+", "-", "*", "/", "(", ")"]

#(A+(B*C))-(D/E)
input = input()
for i in input:
    if i in types:
        if i == ")":
            alphas = ''.join(s for s in alpha)
            alpha.clear()
            result_string = result_string + alphas

            stack_len = len(stack)
            for _ in range(stack_len):
                pop_value = stack.pop()
                if pop_value == "(":
                    continue
                result_string = result_string + pop_value
        else:
            stack.append(i)
    else:
        result_string = result_string + i

if len(alpha) != 0:
    for i in alpha:
        result_string = result_string + i

if len(stack) != 0:
    stack_len = len(stack)
    for i in range(stack_len):
        result_string = result_string + stack.pop()

print(result_string)