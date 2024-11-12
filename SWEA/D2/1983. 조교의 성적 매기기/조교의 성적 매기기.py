# SWEA 1983 조교의 성적 매기기 https://swexpertacademy.com/main/code/problem/problemDetail.do
# n명의 학생이 있으면 n/10명의 학생에게 동일 평점
# 중간 0.35 기말 0.45 과제 0.2
T = int(input())

scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    student = []
    for i in range(n):
        score = list(map(int, input().split()))
        student.append(score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2)

    sorted_student = sorted(student, reverse=True)
    # print(sorted_student)

    k_score = student[k-1]

    # 20명 있으면 2명까지 a+ 30명 있으면 3명까지 a+
    # 그러면 50명 중 idx가 4면? a+ 10이면? a-
    # idx // (n // 10)
    for idx, stu in enumerate(sorted_student):
        if stu == k_score:
            print(f"#{test_case} {scores[idx // (n // 10)]}")