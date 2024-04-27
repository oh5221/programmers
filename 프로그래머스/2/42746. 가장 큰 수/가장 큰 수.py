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
