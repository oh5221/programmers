# 수포자 1: 1 2 3 4 5 -> 5개
# 수포자 2: 2 1 2 3 2 4 2 5 -> 8개 단위 패턴
# 수포자 3: 3 3 1 1 2 2 4 4 5 5 -> 10개 단위 패턴
def solution(answers):
    supoja1 = [1,2,3,4,5]
    supoja2 = [2,1,2,3,2,4,2,5]
    supoja3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0, 0, 0, 0]
    
    for i, ans in enumerate(answers):
        if ans == supoja1[i % len(supoja1)]:
            scores[0] += 1
        if ans == supoja2[i % len(supoja2)]:
            scores[1] += 1
        if ans == supoja3[i % len(supoja3)]:
            scores[2] += 1
        
    max_score = max(scores)
    return [i+1 for i, s in enumerate(scores) if s == max_score]