'''
백설공주와 일곱난쟁이가 살고있었다. 일곱난쟁이가 일하고 돌아왔는데 아홉난쟁이가 됐다
원래 일곱난쟁이는 각각 숫자가 부여되있고 이 수의 합은 100이다.
누가 진짜 일곱 난쟁이 일까

아홉 난쟁이의 총 합을 구하고 이중포문으로 돌아가며 해당 수를 빼 100이 되면 그 둘이 스파이
'''

nanjang_num_list = []
for i in range(9):
    nanjang_num_list.append(int(input()))

total_num = sum(nanjang_num_list)
first_spy = 0
second_spy = 0

for first in range(9):
    for second in range(first + 1, 9):
        temp_sum = nanjang_num_list[first] + nanjang_num_list[second]
        if total_num - temp_sum == 100 :
            first_spy = first
            second_spy = second

for i in range(9):
    if i == first_spy or i == second_spy:
        continue
    print(nanjang_num_list[i])
