def solution(data, ext, val_ext, sort_by):
    # 코드번호, 제조일, 최대수량, 현재수량
    # code / date / maximum / remain
    # ext가 date면 date가 val_ext보다 작을 때, sort_by로 오름차순 정렬
    a = []
    
    for d in data:
        if ext == "code":
            if d[0] <= val_ext:
                a.append(d)
        elif ext == "date":
            if d[1] <= val_ext:
                a.append(d)
        elif ext == "maximum":
            if d[2] <= val_ext:
                a.append(d)
        elif ext == "remain":
            if d[3] <= val_ext:
                a.append(d) 
                
    
    if sort_by == "code":
        return sorted(a, key=lambda x: x[0])
    elif sort_by == "date":
        return sorted(a, key=lambda x: x[1])
    elif sort_by == "maximum":
        return sorted(a, key=lambda x: x[2])
    elif sort_by == "remain":
        return sorted(a, key=lambda x: x[3])