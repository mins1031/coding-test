'''
블랙잭은 21에 가장 가까운 수로 만드는 게임

카드개수 n 과 목표 합 m이 주어질때 카드 3장의 합이 m과 가장 가까운 수 3개의 합을 출력.
3 <= n <= 100
n의 최대수가 매우 작기에 완탐 쌉가능
3중 포문으로 모든 조합을 확인할거임
'''

n , m = map(int, input().split()) # n : 카드의 총 갯수 , m : 카드 3장이 목표로 하는 합
card_list = list(map(int, input().split())) # 카드종류 리스트
max_sum = 0 # 계속 갱신될 최댓값

for first in range(n): # 카드 리스트의 첫번째 기준 카드 인덱스
    for second in range(first+1, n): # 카드 리스트의 두번째 기준 카드 인덱스
        for third in range(second+1, n): # 카드 리스트의 세번째 기준 카드 인덱스
           temp_card_sum = card_list[first] + card_list[second] + card_list[third] # 각 기준 인덱스의 카드 번호를 통해 합을 추출
           if temp_card_sum <= m : # 합이 m을 넘지않는지 체크
               max_sum = max(max_sum, temp_card_sum) # 합과 역대 최댓값을 비교해 더 큰 값이 역대값으로 저장.

print(max_sum)


