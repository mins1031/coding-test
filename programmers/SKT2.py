def solution(periods, payments, estimates):
    answer = [0, 0]
    for i in range(len(periods)):
        join_year = calcul_join_year(periods[i])
        total_payment = sum(payments[i])
        next_year_payment = total_payment - payments[i][0] + estimates[i]
        # if calcul_join_year(periods[i] + 1) == 2 :
        #     if next_year_payment >= 900000:
        #         answer[0] += 1
        # elif calcul_join_year(periods[i] + 1) == 5:
        #     if next_year_payment >= 600000:
        #         answer[0] += 1
        if join_year >= 5:
            if total_payment < 600000 and next_year_payment >= 600000:
                answer[0] += 1
            elif total_payment >= 600000 and next_year_payment < 600000:
                answer[1] += 1
        elif 5 > join_year >= 2:
            if calcul_join_year(periods[i]+1) == 5:
                if next_year_payment >= 600000:
                    answer[0] += 1
            if total_payment < 900000 and next_year_payment >= 900000:
                answer[0] += 1
            elif total_payment >= 900000 and next_year_payment < 900000:
                answer[1] += 1
        elif 5 > calcul_join_year(periods[i] + 1) >= 2:
            if next_year_payment >= 900000:
                answer[0] += 1
        # elif calcul_join_year(periods[i] + 1) >= 5:
        #     if next_year_payment >= 600000:
        #         answer[0] += 1

    return answer


def calcul_join_year(month_count):
    return month_count // 12


# periods = [20, 23,24]
# payments = [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
#             [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
#             [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]]
# estimates = [100000, 100000, 100000]
# print(solution(periods, payments, estimates))

periods2 = [24, 59, 59, 60]
payments2 = [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
             [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
             [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
             [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]]
estimates2 = [350000, 50000, 40000, 50000]
print(solution(periods2, payments2, estimates2))

'''
1. 이번달은 VIP가 아니지만 다음달에 VIP가됨  
  -> 해당 고객의 가입기간에 따라 기준이 달라짐 
   1) 5년이상이고 이번달은 60미만이지만 다음달 지급액이 60이상인경우,
   2) 2년 이상 5년 미만이고 이번달은 90 미만이지만 다음달은 90 이상인경우,
   이 두개가 1번 요건을 충족하는 조건
2. 이번달은 VIP지만 다음달은 VIP가 아님
 -> 이또한 고객의 가입기간에 따라 기준이 달라짐
  1) 5년이상이고 이번달은 60이상이지만 다음달을 60 미만인 경우
  2) 2년 ~ 5년 미만 이고 이번달은 90이상이지만 다음달은 90 미만인 경우 

해서 결과배열은 2줄에 1줄이 1번의 카운트 2줄이 2번의 카운드이다
해서 1번부터 새서 넣고 2번새서 넣고 하나느게 베스트?
아니면 한번만 돌면서 1,2 번 동시에 판단해야 할듯
그럼 가입기간보고 나누고 -> 이번달금액이랑 다음달 금액보고 조건으로 나눠서 연산해야 할듯   
'''