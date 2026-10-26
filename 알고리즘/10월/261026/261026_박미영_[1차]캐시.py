# cacheSize : 캐시 크기
# cities : 도시이름 배열
# 캐시 크기에 따른 실행시간 측정 
# 캐시 교체 알고리즘은 LRU
# cache hit : 찾는 데이터가 캐시에 있음
# cache miss : 찾는 데이터가 캐시에 없음 
# 도시 이름은 대소문자 구분 X

def solution(cacheSize, cities):
    cache = [] # 캐시, 제일 처음이 옛날 거, 제일 마지막이 최근에 쓴 거
    answer = 0 # 실행 시간
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city_l = city.lower()
        if city_l in cache: # cache hit
            cache.remove(city_l)
            cache.append(city_l)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city_l)
            answer += 5
            
    return answer
