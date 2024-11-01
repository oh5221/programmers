# n * n 배열
# arr1과 arr2를 각각 인덱스에 맞게 | 계산
# 각 숫자를 2진수화
# 1이면 # 0이면 공백
def solution(n, arr1, arr2):
    answer = []
    
    # or 연산 및 2진수화
    for i in range(n):
        row = bin(arr1[i] | arr2[i])[2:].zfill(n)
        
        row = row.replace('1', '#').replace('0', ' ')
        
        answer.append(row)
        
    return answer