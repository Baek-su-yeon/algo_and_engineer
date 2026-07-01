# 문제 1
# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string, letter):
    answer = ''
    
    for my_letter in my_string:
        
        if my_letter == letter: continue
        
        answer += my_letter
    
    return answer

# 더 간단한 풀이
def solution(my_string, letter):
    return my_string.replace(letter, '')

# 문제 2
# 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.
def solution(age):
    answer = ''
    
    # 아스키 코드 0 ~ 9: 48 ~ 57
    # 아스키 코드 a ~ j: 97 ~ 106
    for num_str in str(age):
        temp = ord(num_str) + ord('a') - ord('0')
        answer += chr(temp)
        
    
    return answer


# 문제 3
# 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.
def solution(emergency):
    answer = [0] * len(emergency)

    sorting_emergency = sorted(emergency, reverse=True)
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if sorting_emergency[i] == emergency[j]:
                answer[j] = i + 1
    
    return answer

# 더 깔끔한거는
def solution(emergency):
    return [sorted(emergency, reverse=True).index(num) + 1 for num in emergency]