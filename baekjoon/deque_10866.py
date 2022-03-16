import sys

n = int(sys.stdin.readline())
deque = []
for _ in range(n):
    command = sys.stdin.readline().rstrip().split(" ")
    if command[0] == "push_front":
        deque.insert(0, command[1])
    elif command[0] == "push_back":
        deque.append(command[1])
    elif command[0] == "pop_front":
        if not deque:
            print("-1")
            continue
        print(deque[0])
        del deque[0]
    elif command[0] == "pop_back":
        if not deque:
            print("-1")
            continue
        print(str(deque.pop()))
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        if not deque:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if not deque:
            print("-1")
            continue
        print(deque[0])
    elif command[0] == "back":
        if not deque:
            print("-1")
            continue
        print(deque[-1])



