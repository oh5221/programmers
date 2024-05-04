# 시간초과
# arr = list(range(1, int(input()) + 1))
#
# while len(arr) != 1:
#     arr.pop(0)
#     arr.append(arr.pop(0))
#
# print(arr[0])

from collections import deque
queue = deque(range(1, int(input()) + 1))

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())
