'''
스위치가 있음
스위치 :  0 1 0 1 0 0 0 1

남학생 자기가 받은 배수 번호 스위치 값을 바꾼다 ex -> 3을 받으면 3번, 6번 스위치의 값을 바꿈
여학생은 자기가 받은 번호를 기준으로 양옆의 값이 대칭인 최대구간의 스위치 값을 바꾼다. ex -> 3번을 받았다면 2,4번의 수가 같음 (= 1) 같으니 다음 양옆값을 봄 1,5값을 보면 같음 (= 0) 그래서 1~5까지ㅏ의 값을 바꾸게됨.
이렇게 바꾼후 스위치의 상태를 출력.
'''

n = int(input()) # 스위치 갯수
switch = list(map(int, input().split())) # 스위치 값들
switch.insert(0,0)
student_count = int(input()) # 학생수

def switching(index) :
    if switch[index] == 0:
        switch[index] = 1
    else:
        switch[index] = 0

for i in range(student_count):
    gender, switch_index = map(int, input().split())
    if gender == 1:
        for j in range(1, n):
            target_index = (switch_index * j)
            if target_index > n :
                break
            switching(target_index)
    else:
        right_target_index = switch_index
        left_target_index = switch_index
        switching(switch_index)
        for j in range(1, n):
            right_target_index = right_target_index + 1
            left_target_index = left_target_index - 1
            if 1 > left_target_index or n < right_target_index:
                break

            if switch[left_target_index] == switch[right_target_index] :
                switching(left_target_index)
                switching(right_target_index)
            else:
                break
switch.pop(0)

for i in range(1, n+1):
    print(switch[i-1], end=" ")
    if (i % 20) == 0 :
        print("")



