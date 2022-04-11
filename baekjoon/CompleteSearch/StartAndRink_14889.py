# # iteratool 없이 구현 -> 순열을 모두 구하는 로직을 직접구현
# def cal_diff(team1, team2):
#     sum_team1 = 0
#     sum_team2 = 0
#
#     for i in range(len(team1)):
#         for j in range(len(team1)):
#             sum_team1 += arr[team1[i]][team1[j]]
#             sum_team2 += arr[team2[i]][team2[j]]
#
#     return abs(sum_team1 - sum_team2)
#
# def make_team(team1, count, N, start):
#     global answer
#
#     if count == N//2:
#         team2 = []
#         for i in range(N):
#             if i not in team1:
#                 team2.append(i)
#
#         local_diff = cal_diff(team1, team2)
#         answer = min(answer, local_diff)
#         return
#
#     for i in range(start, N):
#         if i not in team1:
#             team1.append(i)
#             make_team(team1, count+1, N, i+1)
#             team1.remove(i)
#
# if __name__=="__main__":
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     answer = int(1e9)
#     make_team([], 0, N, 0)
#
#     print(answer)

# iteratool 사용한 로직 -> 순열 조합을 미리 만들어놓고 구하는 방식
from itertools import combinations  # 조합 함수

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []

# 조합으로 가능한 팀 생성해주기
for team in list(combinations(members, N // 2)):
    possible_team.append(team)

min_stat_gap = 10000  # 갭이 가장 작은 값을 찾기 위하여
for i in range(len(possible_team) // 2):
    # A 팀
    team = possible_team[i]
    stat_A = 0  # A팀 능력치
    for j in range(N // 2):
        member = team[j]  # 멤버
        for k in team:
            stat_A += S[member][k]  # 멤버와 함께할 경우의 능력치들

    # A를 제외한 나머지 팀
    team = possible_team[-i - 1]
    stat_B = 0
    for j in range(N // 2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]

    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))

print(min_stat_gap)