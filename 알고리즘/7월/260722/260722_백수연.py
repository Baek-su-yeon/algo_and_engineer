def solution(my_string):
    answer = []
    
    for letter in my_string:
        if letter.isdigit():
            answer.append(int(letter))
        
    return sorted(answer)