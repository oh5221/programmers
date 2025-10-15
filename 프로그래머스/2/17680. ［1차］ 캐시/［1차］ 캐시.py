# DB캐시 적용 시 캐시 크기에 따른 실행시간 측정
# LRU 사용 (가장 사용 안 한 거 삭제)
# cache hit -> 1 / cache miss -> 5
def solution(cacheSize, cities):
    answer = 0
    cache = [] * cacheSize
    
    for idx, city in enumerate(cities):
        city = city.lower()
        if cacheSize == 0:
            return 5 * len(cities)
        if len(cache) == cacheSize:
            if city in cache:
                answer += 1
                cache.pop(cache.index(city))
                cache.append(city)
            else:
                answer += 5
                if cache:
                    cache.pop(0)
                cache.append(city)
        if len(cache) < cacheSize:        
            if city in cache:
                answer += 1
                cache.pop(cache.index(city))
                cache.append(city)
            else:
                answer += 5
                cache.append(city)
        # print(cache)
    
    return answer