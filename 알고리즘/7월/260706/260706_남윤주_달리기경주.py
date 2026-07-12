'''
현재 순위 players
해설진이 부른 callings 한 번 부를 때마다 불린 사람은 순위 하나 오르고 불린 사람 앞 사람은 순위 하나 내려감
사람별 순위를 바꾸면 되나
a를 부르면 a 순위를 -1 해주고 해당 순위에 있던 사람의 순위를 +1 해주고
{a:2} {b:1}
{2:a} {1:b}

{a:1} 바꾸고 {1:b}에서 b를 찾아서 {b:2}로 바꾸고 {1:a}랑 {2:b}로 바꾸고
'''
def solution(players, callings):
    # enumerate 이용하여 선수별 rank 찾기
    player_rank = {player: i for i, player in enumerate(players)}
    
    for person in callings:
        # 불린 사람 기존 순위
        cur_idx = player_rank[person]
        # 불린 사람 앞 사람
        front_idx = cur_idx - 1
        
        front_player = players[front_idx]
        
        players[cur_idx], players[front_idx] = players[front_idx], players[cur_idx]
    
        player_rank[person] = front_idx
        player_rank[front_player] = cur_idx
        
    return players