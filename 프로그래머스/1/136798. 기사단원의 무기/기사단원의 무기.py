# number의 약수의 개수에 해당하는 공격력(power)
# 근데 약수 개수가 limit보다 크면 power에 해당하는 공격력의 무기를 가져야 함
# power 1당 1kg의 철이 필요함
# 모든 무기를 만들기 위해 필요한 철의 무게는?
def solution(number, limit, power):
    answer = 0
    powers = []
    
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                cnt += 1
                if j != i // j:  # j와 i // j가 다를 때만 두 개의 약수 추가
                    cnt += 1
        powers.append(cnt)
    
    for p in powers:
        if p > limit:
            answer += power
        else:
            answer += p
    
    return answer
