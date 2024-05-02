n = int(input()) # 3
line = list(map(int, input().split())) # [2, 1, 3]

wait = [] # 추가 공간
snack = 1 # 간식 받을 사람

while line:
    if line[0] == snack: # 제 순서일 때
        line.pop(0) # 그냥 빼냄
        snack += 1 #다음 순서로

    else:
        if wait and wait[-1] == snack:
            # wait 쪽에서 마지막에 서 있는 애가 제 순서일 때
            wait.pop()
            snack += 1
        if not wait or wait[-1] != snack:
            wait.append(line[0])
            line.pop(0)
            
while wait:
    if wait[-1] != snack:
        print('Sad')
        break
    else:
        wait.pop()
        snack += 1

if not wait:
    print('Nice')