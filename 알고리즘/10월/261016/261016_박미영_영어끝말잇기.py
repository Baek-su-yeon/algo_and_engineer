# 마지막 사람이 말하면 다시 1번부터 시작
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 함.
# 이전에 등장했던 단어는 ㄴㄴ
# 한 글자 단어 ㄴㄴ
# n : 사람 수
# words : 사람들이 순서대로 말한 단어
# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지 출력 : [번호, 차례]

def solution(n, words):
    number = 0
    order = 0
    
    for i in range(len(words) - 1):
        if words[i][-1] != words[i+1][0] or words[i+1] in words[:i+1] or len(words[i+1]) == 1:
            number = (i+1) % n + 1
            order = int((i+1) // n) + 1
            break
            
    return (number, order)
            
