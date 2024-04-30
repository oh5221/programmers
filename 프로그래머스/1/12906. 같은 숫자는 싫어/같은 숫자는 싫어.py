def solution(arr):
    answer = []
    idx = 0
    for i in range(len(arr)):
        if arr[idx] != arr[i]:
            answer.append(arr[idx])
            idx = i
    answer.append(arr[idx])
    
    return answer