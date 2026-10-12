# phone_book : 전화번호부에 적힌 전화번호를 담은 배열
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
# 그렇지 않으면 true 출력 

def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        l = len(phone_book[i])
        
        if phone_book[i] == phone_book[i+1][:l]:
            return False
        
    return True
