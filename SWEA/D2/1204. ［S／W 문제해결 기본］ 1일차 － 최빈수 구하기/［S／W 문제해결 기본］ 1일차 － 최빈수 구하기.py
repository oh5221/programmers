T = int(input())
for test_case in range(1, T+1):
    _ = int(input()) # 테스트 케이스 번호 -> input 무시
    students = list(map(int, input().split()))
    scores = [0] * 101

    for s in students:
        scores[s] += 1
    
    mode_num = max(scores) # 최빈수는 몇개씩있는지
    max_num = 0
    for idx, num in enumerate(scores):
        if num == mode_num:
            if max_num < idx:
                max_num = idx

    print(f"#{test_case} {max_num}")