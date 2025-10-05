# 길이가 긴 쪽을 반으로 접음
# 접고 소수점 이하는 버림. 돌려서 지갑에 넣을 수 있다면 그만함
def solution(wallet, bill):
    answer = 0
    # 26, 17 -> 13, 8
    while True:
        bill.sort(reverse=True)
        wallet.sort(reverse=True)
        
        if bill[0] > wallet[0] or bill[1] > wallet[1]:
            bill[0] = bill[0] // 2
            # print(f"지갑: {wallet} 지폐: {bill}")
            answer += 1
        else:
            return answer