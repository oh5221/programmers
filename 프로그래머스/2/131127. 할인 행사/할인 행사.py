# 금액 지불 -> 10일 회원 자격
# 한 가지 제품 할인 (1개만 구매 가능)
# 원하는 제품과 수량이 할인하는 날짜랑, 10일 연속으로 일치하면 -> 회원가입
def solution(want, number, discount):
    answer = []
    dictionary = {want[i]:number[i] for i in range(len(number))}
    # print(dictionary)
    
    for idx in range(0, len(discount)-len(want)):
        dis = discount[idx:idx+10]
        dic = {want[i]:0 for i in range(len(number))}
        for d in dis:
            if d in dic:
                dic[d] += 1
            else:
                pass
        
        # print(idx, dic)
        if dic == dictionary:
            answer.append(idx + 1)
    
    
    return len(answer)