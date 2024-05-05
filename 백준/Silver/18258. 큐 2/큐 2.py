import sys
from collections import deque
n = int(sys.stdin.readline()) # 명령 개수
arr = deque()

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        arr.append(int(command[1]))

    elif command[0] == "pop":
        if arr:
            print(arr.popleft())
        else:
            print(-1)

    elif command[0] == "size":
        print(len(arr))

    elif command[0] == "empty":
        if arr:
            print(0)
        else:
            print(1)

    elif command[0] == "front":
        if arr:
            print(arr[0])
        else:
            print(-1)

    elif command[0] == "back":
        if arr:
            print(arr[-1])
        else:
            print(-1)