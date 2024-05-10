def solution(answers):
    # 수포자 1 : 1 2 3 4 5 반복
    # 수포자 2 : 2 / 1 2 3 / 2 / 4 / 2 / 5  반복
    # 수포자 3: 3 3 / 1 1 / 2 2 / 4 4 / 5 5  반복 (3-1-2-4-5)

    su1 = [1, 2, 3, 4, 5]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answer = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == su1[i%len(su1)]:
            answer[0] += 1
        if answers[i] == su2[i%len(su2)]:
            answer[1] += 1
        if answers[i] == su3[i%len(su3)]:
            answer[2] += 1

    print(answer)
    result = []
    for idx, ans in enumerate(answer):
        if max(answer) == ans:
            result.append(idx + 1)
    
    return result