from itertools import permutations
import math
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def solution(numbers):
    # 숫자 조각으로 만들 수 있는 수를 구한다
    # 이 숫자들이 소수인지 아닌지 판별한다
    count = 0
    # 중복 없어야 하니까 set
    nums = set()
    # numbers
    numbers = list(numbers)
    print(numbers)
    
    # 숫자 조합
    for i in range(1, len(numbers)+1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            nums.add(num)
    print(nums)
    
    # 소수 체크
    for num in nums:
        if isPrime(num):
            count += 1
            
    return count