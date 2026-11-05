from heapq import heappop, heappush

def solution(genres, plays):
    new_list = []
    just_before_answer = []
    set_genres = dict.fromkeys(genres, 0)
    
    for i, genre in enumerate(genres):
        new_list.append((-plays[i], i, genre))
        set_genres[genre] += plays[i]
    
    sorted_genres = sorted(
        set_genres, key=set_genres.get, reverse=True
    )
    
    answer = []
    
    for genre in sorted_genres:
        genre_songs = [
            (n, idx) for n, idx, g in new_list if g == genre
        ]
        
        genre_songs.sort()
        
        for n, idx in genre_songs[:2]:
            answer.append(idx)
    return answer