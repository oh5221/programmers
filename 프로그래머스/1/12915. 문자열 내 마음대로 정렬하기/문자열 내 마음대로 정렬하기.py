def solution(strings, n):
    # 특정 문자열을 기준으로 정렬
    # https://velog.io/@dlsdud9098/python-sorted-sort-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0
    
    return sorted(strings, key=lambda x: (x[n], x))