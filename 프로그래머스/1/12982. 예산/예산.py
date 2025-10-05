# budget이랑 완전 똑같으면서, 개수가 많아야함
# 시간 생각 안하면 -> permutations로 sum이 budget이랑 동일할때만 ... 그래서 len() -> 시간초과
# 시간 생각하면 -> sum(d)와 budget 간의 차이 구하기
# sum(d) - budget이랑 동일한 값이 나오는 경우의 수?
def solution(d, budget):
    answer = 0 
    d.sort()
    
    while budget < sum(d):
        d.pop()
        print(d)


    return len(d)