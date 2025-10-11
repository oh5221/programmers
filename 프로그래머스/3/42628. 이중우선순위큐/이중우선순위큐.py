# I 숫자 (숫자삽입) D 1(최댓값삭제) D -1 (최솟값삭제)
# 큐가 비면 [0,0] 아니면 [최대,최소] return
from collections import deque
def solution(operations):
    answer = []
    nums = deque()
    
    for op in operations:
        command, num = op.split()
        num = int(num)
        
        if command == "I":
            nums.append(num)
            nums = sorted(nums)
        elif command == "D":
            if nums:
                if num == 1:
                    nums.pop()
                elif num == -1:
                    nums = nums[1:]
            else:
                continue
    return [0, 0] if not nums else [max(nums), min(nums)]