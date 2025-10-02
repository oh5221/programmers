# 종이 조각으로 만들 수 있는 소수
from itertools import permutations
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    nums = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            nums.add(num)
    # print(nums)
    
    for num in nums:
        if isPrime(num) == True:
            answer += 1
    return answer