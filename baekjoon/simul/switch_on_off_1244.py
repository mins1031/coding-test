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

def switching(index) : # 받은 인덱스의 값을 바꾸는 함수
    if switch[index] == 0:
        switch[index] = 1
    else:
        switch[index] = 0

for i in range(student_count):
    gender, switch_index = map(int, input().split()) # 학생의 성별과 스위치 인덱스 번호를 입력받는다.
    if gender == 1: # 남학생의 경우
        for j in range(switch_index, n, switch_index): # 배수의 인덱스의 내용을 스위칭 해야하기 때문에 스위치 인덱스부터 인덱스 값만큼 늘려가는 포문으로 구현한다.
            switching(j) # 해당해서 나온 인덱스 위치의 데이터를 스위칭한다.
    else: # 여학생의 경우
        switching(switch_index) # 우선 입력받은 위치는 무조건 스위칭이기 때문에 스위치 함수를 호출한다.
        for j in range(n//2): # 입력받은 인덱스 양쪽 두 위치부터 검사해 가기 때문에 스위치 길이의 / 2 만큼 검사한다.
            if 1 > (switch_index - j) or n < (switch_index + j): # 만약 적용해보려는 위치가 스위치 길이를 벗어나게 되면 스위칭을 종료 시킨다.
                break

            if switch[switch_index - j] == switch[switch_index + j] : # 만약 양쪽 인덱스 스위치의 값이 같다면 양 스위치 값을 변경하고 포문을 지속한다.
                switching(switch_index - j)
                switching(switch_index + j)
            else: # 만약 양쪽 인덱스 값이 다르다면 스위칭 작업을 종료한다.
                break

for i in range(1, n+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()



