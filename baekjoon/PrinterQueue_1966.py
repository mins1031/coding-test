'''
result = list()
for i in range(test_case):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))

    temp = m
    order_cnt = 0
    while True:
        largest = max(docs)
        if docs[0] < largest:
            if temp == 0:
                docs.append(docs.pop(0))
                temp = n - 1
                continue
            docs.append(docs.pop(0))
            temp -= 1
        elif docs[0] == largest:
            if temp == 0:
                order_cnt += 1
                break
            order_cnt += 1
            docs.pop(0)
            temp -= 1

    result.append(order_cnt)

for i in result:
    print(i)
'''
test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split(' '))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    cnt = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            cnt += 1
            if queue[0][1] == m:
                print(cnt)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

