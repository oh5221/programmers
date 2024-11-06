# 1204 최빈수 구하기
# 1000명 수학 성적을 토대로
import statistics
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    scores = list(map(int, input().split()))
    scores.sort()
    cnt, max_value = 0, 0
    for score in scores:
        if scores.count(score) > cnt:
            cnt = scores.count(score)
            max_value = score
        if scores.count(score) == cnt:
            max_value = max(max_value, score)
    # score = statistics.mode(scores) # 뭔가 오류가 있는 듯 RuntimeError 뜸
    print(f"#{n} {max_value}")
