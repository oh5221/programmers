import heapq

def solution(scoville, K):
    answer = 0
    mix_scoville = 0
    heapq.heapify(scoville)         # 최초 리스트에서 힙 정렬
    
    while scoville[0] < K: # 가장 작은 값이 K보다 크면 종료
        if(len(scoville)<2): # list에 적어도 값 2개는 있어야함
            return -1
        mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville,mix_scoville)           
        answer +=1                          
        
    return answer