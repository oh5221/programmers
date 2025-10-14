# 후보키(유일성 + 최소성) 
from itertools import combinations
def solution(relation):
    row, col = len(relation), len(relation[0])
    candidates = []
    unique = []
    visited = [0] * col
    
    
    for i in range(1, col+1):
        candidates.extend(combinations(range(col), i))
    
    # print(candidates)
    
    
    for candi in candidates:
        tmp = [tuple(item[idx] for idx in candi) for item in relation]
        if len(set(tmp)) == row:
            unique.append(candi)
            
    # print(unique)
    
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(set(unique[i])) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
                
    return len(answer)