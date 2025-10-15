# 튜플 -> 중복가능, 순서없음, 순서다르면 다른튜플, 개수는 유한
# n개의 원소 개수에서, 중복되는 원소가 없는 튜플이 있을 때 집합으로 그리기
def solution(s):
    answer = []
    
    s = s.split("},{")
    s = [d.replace("{", "").replace("}", "") for d in s]
    s.sort(key=lambda x:len(x))
    # print(s)
    
    for num in s:
        for n in num.split(","):
            if int(n) not in answer:
                answer.append(int(n))
                

    return answer