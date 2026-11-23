# 최소한의 객실만을 사용하여 예약 손님들을 받을거임.
# 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소하고 다음 손님 사용 가능
# book_time : 예약 시각이 문자열 형태로 담긴 2차원 배열
# 코니에게 필요한 최소 객실의 수 

def solution(book_time):
    room = [] # room[i] : i번 방의 퇴실 시간
    # 결과적으로 len(room) 출력하면 답 나오지 않을까
    
    for book in book_time:
        start, finish = book[0], book[1]
        start_h, start_m = start.split(":")
        book[0] = int(start_h) * 60 + int(start_m)
        finish_h, finish_m = finish.split(":")
        book[1] = int(finish_h) * 60 + int(finish_m)
    
    book_time.sort(key=lambda x : x[0])
    
    for book in book_time:
        if not room:
            room.append(book[1])
        else:
            for i in range(len(room)):
                if room[i] + 10 <= book[0]:
                    room[i] = book[1]
                    break
            else:
                room.append(book[1])
    
    return len(room) 
