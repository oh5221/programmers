# 숫자를 한자리수로 만들어서 -> 더 큰 숫자를 먼저 넣음
# 들어간 숫자는 numbers에서 pop됨
# 맨 첫번째 수가 같다면(ex. 30, 34)
# 3430이랑 3034 중에 대소비교해서 넣기
from itertools import permutations
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*4, reverse=True)
    
    # for i in range(len(numbers)-1):
    #     # 바꿨을 때 더 큰 수가 나오면 바꿈
    #     if numbers[i]+numbers[i+1] < numbers[i+1]+numbers[i]:
    #         numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    
    return ''.join(numbers) if numbers[0] != '0' else '0'