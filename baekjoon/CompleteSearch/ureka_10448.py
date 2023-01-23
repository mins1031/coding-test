import time
start_time = time.time()	# 측정 시작

n = int(input())
triangle_num = [1]
input_list = []
same_candy_max_count = []

for i in range(n) :
    input_list.append(int(input()))

start_num = 2
for input in range(0, 5000) :
    before_tri_num = triangle_num[input]
    if before_tri_num + start_num > 1000:
        break

    triangle_num.append(before_tri_num + start_num)
    start_num += 1

for input in input_list:
    is_find_max = False
    for i in range(len(triangle_num)):
        for j in range(len(triangle_num)):
            for p in range(len(triangle_num)):
                temp_sum = triangle_num[i] + triangle_num[j] + triangle_num[p]
                if temp_sum == input :
                    is_find_max = True
                    print(1)
                    break
            if is_find_max:
                break
    if not is_find_max:
        print(0)

end_time = time.time()		# 측정 종료
print('time:', end_time - start_time)	# 수행 시간 출력

# 5
# 4
# 6
# 11
# 20
# 29