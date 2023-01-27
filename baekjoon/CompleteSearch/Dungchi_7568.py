'''
A와 B는 각각 A(177cm, 76kg)=(177,76) , B(173cm, 71kg)=(173,71) 이다. 이경우 A가 B보다 덩치가 크다 라고 할수 있다.
근데 이렇게 딱 떨어지는게 아닌  A = (175, 67), B= (177, 59) 면 누구의 덩치가 더 큰건가? 누구도 상대보다 크다고 할수 없다.

각 키와 몸무게를 입력받음.
1. 키 몸무게 두 개로 돌면서 기준보다 덩치가 큰 수를 카운팅함.
2. 리스트 다돌고 순위 리스트에 카운팅된 수 +1로 추가
'''

n = int(input()) # 총 학생의 수. 최대50
dungchi_list = [] # 키와 몸무게를 입력받을 리스트
rank_list = [] # 순위를 저장할 리스트

for i in range(n):
    student_dungchi = list(map(int, input().split()))
    dungchi_list.append(student_dungchi)
    rank_list.append(0) # 학생별 덩치를 입력받고 추후 계산시 편하게 인덱스를 맞추기 위해 순위 리스트도 0으로 초기화한다.

for i in range(n):
    more_big_count = 0  # 리스트내에서 기준보다 덩치가 큰 학생의 수
    stand_mom = dungchi_list[i][0] # 기준 몸무게
    stand_key = dungchi_list[i][1] # 기준 키
    for j in range(n):
        if j == i : # 기준과 같은 인덱스 즉 같은 값을 비교할 필요는 없으니 패스
            continue
        if dungchi_list[j][0] > stand_mom and dungchi_list[j][1] > stand_key: # 만약 기준보다 덩치가 큰 값을 만나면 큰 학생수 +1
            more_big_count += 1
    rank_list[i] = more_big_count + 1 # 나보다 덩치 큰 학생 +1이 나의 순위이다.

for i in rank_list:
    print(i)
