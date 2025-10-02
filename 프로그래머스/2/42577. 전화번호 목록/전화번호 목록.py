# phone_book에서 한 번호가 다른 번호의 접두어라면 false, 아니면 true
# 정렬해서? 필요없나?
# 2중 for문으로 체크...?
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True