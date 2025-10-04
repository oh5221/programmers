# n편 중 h번 이상 인용된 논문이 h편 이상
# 나머지가 h번 이하라면 h의 최댓값
# 
def solution(citations):
    citations.sort(reverse=True)
    
    for idx, num in enumerate(citations):
        if idx >= citations[idx]:
            return idx
    
    return len(citations)