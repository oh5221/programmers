def solution(num_list):
    odd = ""
    even = ""
    
    for idx, i in enumerate(num_list):
        if i % 2 == 1:
            odd += str(i)
        else:
            even += str(i)
    
    return int(odd) + int(even)