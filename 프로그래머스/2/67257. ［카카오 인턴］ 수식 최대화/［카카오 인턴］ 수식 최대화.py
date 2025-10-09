# 숫자, +-* 주어짐. 연산자 우선순위를 재정의해서 만들 수 있는 가장 큰 숫자는?
import re
def solution(expression):
    answer = 0
    expr = re.findall(r'\d+|[+\-*/()]', expression)
    checks = [["*", "+", "-"], ["*", "-", "+"],
              ["+", "*", "-"], ["+", "-", "*"],
              ["-", "*", "+"], ["-", "+", "*"]]
    
    for check in checks:
        # print(f"현재 우선순위: {check}")
        test_expr = expr.copy()
        while check[0] in test_expr:
            idx = test_expr.index(check[0])
            if check[0] == '+':
                num = int(test_expr[idx-1]) + int(test_expr[idx+1])
            elif check[0] == '*':
                num = int(test_expr[idx-1]) * int(test_expr[idx+1])
            elif check[0] == '-':
                num = int(test_expr[idx-1]) - int(test_expr[idx+1])
            test_expr.insert(idx-1, num)
            del test_expr[idx : idx + 3]
        # print("우선순위 첫번째 완료:", test_expr)
        while check[1] in test_expr:
            idx = test_expr.index(check[1])
            if check[1] == '+':
                num = int(test_expr[idx-1]) + int(test_expr[idx+1])
            elif check[1] == '*':
                num = int(test_expr[idx-1]) * int(test_expr[idx+1])
            elif check[1] == '-':
                num = int(test_expr[idx-1]) - int(test_expr[idx+1])
            test_expr.insert(idx-1, num)
            del test_expr[idx : idx + 3]
        # print("우선순위 두번째 완료:", test_expr)
        while check[2] in test_expr:
            idx = test_expr.index(check[2])
            if check[2] == '+':
                num = int(test_expr[idx-1]) + int(test_expr[idx+1])
            elif check[2] == '*':
                num = int(test_expr[idx-1]) * int(test_expr[idx+1])
            elif check[2] == '-':
                num = int(test_expr[idx-1]) - int(test_expr[idx+1])
            test_expr.insert(idx-1, num)
            del test_expr[idx : idx + 3]
        # print("우선순위 세번째 완료:", test_expr)
        
        if abs(test_expr[0]) > answer:
            answer = abs(test_expr[0])
    
    
    
    return answer