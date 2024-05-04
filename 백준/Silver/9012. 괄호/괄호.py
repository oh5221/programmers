t = int(input())
ps = ""

def if_Ps(ps):
    if ps[0] == ")" or ps[-1] == "(":
        return False
    elif ps.count("(") != ps.count(")"):
        return False
    else:
        stack = []
        for i in ps:
            if i == '(':
                stack.append(i)
            else:
                if not stack:
                    return False
                    break
                else:
                    stack.pop()
    return True

for i in range(t):
    ps= input()

    if if_Ps(ps):
        print('YES')
    else:
        print('NO')