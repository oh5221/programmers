import functools

def compare(num1, num2):
    # 좌측이 크면 -1을 return해서 내림차순 정렬
    # 정렬을 수동 구현하지 않아도 됨 -> 오류 줄어듦
    if num1+num2 > num2+num1:
        return -1
    else:
        return 1
    
def solution(numbers):
    # int 배열을 str로 변환한다
    numbers = list(map(str, numbers))
    
    numbers.sort(key=functools.cmp_to_key(compare))
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    else:
        return answer


    
    '''  
    # 하나씩 확인하면서 a+b가 b+a보다 작으면 swap
    # 한 번의 for문으로 정렬이 되지 않고 시간이 오래 걸리므로 폐기
    for i in range(len(numbers) - 1):
        if numbers[i] + numbers[i+1] <= numbers[i+1] + numbers[i]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    
    # print(numbers)
    
    # answer에 숫자 차례대로 넣기
    for num in numbers:
        answer += num
    '''
    
    '''
     # numbers = sorted(numbers) 기준 앞뒤 숫자로 비교한 코드
    for i in range(len(numbers)):
        if (answer + numbers[i]) >= (numbers[i] + answer):
            answer = (answer + numbers[i])
            # print(answer)
        else:
            answer = (numbers[i] + answer)
            # print(answer)
    
    '''
    

'''
# 순열 사용한 풀이 -> 출력 초과로 폐기
from itertools import permutations
def solution(numbers):
    nums = list(map(str, numbers))
    # print(nums)
    
    permu_num = list(map(''.join,permutations(nums, len(nums))))
    
    return max(permu_num)
'''
