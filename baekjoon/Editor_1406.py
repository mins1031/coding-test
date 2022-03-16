import sys
from collections import deque

left_stack = list(sys.stdin.readline().rstrip())
right_stack = deque()
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().strip().split(" ")
    if command[0] == 'L':
        if not left_stack:
            continue
        right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if not right_stack:
            continue
        left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if not left_stack:
            continue
        left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])

print("".join(left_stack + list(reversed(right_stack))))

# ans
# dmiqnasmn