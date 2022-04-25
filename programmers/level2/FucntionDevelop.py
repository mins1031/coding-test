from collections import deque
'''
def sol(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        while len(progresses) != 0 and progresses[0] >= 100:
            cnt += 1
            progresses.popleft()
        if cnt != 0:
            answer.append(cnt)
    return answer
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
명답 이중포문 사용 않고도 해결;
한번더 풀어볼것
'''

def sol(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses) > 0:
        if(progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for _ in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                cnt += 1
        if cnt != 0 :
            answer.append(cnt)
    return answer


progresses =[95, 90, 99, 99, 80, 99]
progresses2 = [93, 30, 55]
speeds =[1,1,1,1,1,1]
speeds2 = [1, 30, 5]

print(solution(progresses2, speeds2))
