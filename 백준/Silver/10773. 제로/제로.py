num_len = int(input())
number = []
for i in range(num_len):
    num = int(input())
    if num != 0:
        number.append(num)
    else:
        number.pop()

answer = sum(number)
print(answer)