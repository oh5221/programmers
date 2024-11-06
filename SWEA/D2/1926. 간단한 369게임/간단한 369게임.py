T = int(input())
for test_case in range(1, T + 1):
    cnt_3 = str(test_case).count('3')
    cnt_6 = str(test_case).count('6')
    cnt_9 = str(test_case).count('9')
    cnt = cnt_3 + cnt_6 + cnt_9
    if cnt == 0:
        print(test_case, end=' ')
    else:
        print('-' * cnt, end=' ')