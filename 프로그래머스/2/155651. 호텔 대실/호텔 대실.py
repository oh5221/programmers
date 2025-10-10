# 퇴실시간 + 10분 청소 -> 다시 예약 가능
# 최소 객실 수는?
from heapq import heappop, heapify, heappush
def solution(book_time):
    answer = 0
    books = []
    rooms = []
    for book in book_time:
        lst = []
        hour, minute = book[0].split(":")
        lst.append(int(hour) * 60 + int(minute)) # 시작시간
        hour, minute = book[1].split(":")
        lst.append(int(hour) * 60 + int(minute) + 10) # 퇴실 + 청소시간
        books.append(lst)
    
    books.sort()
    # print(books)
    
    for book in books :
        check_in = int(book[0])
        check_out = int(book[1])
        if len(rooms) != 0 and rooms[0] <= check_in: # 입실시간이 이전이용자 퇴실 이후면
            heappop(rooms) # 원래 있던 퇴실시각 뺌
        heappush(rooms,check_out) # 퇴실 시각만 넣음
        # print(rooms)
    return len(rooms)