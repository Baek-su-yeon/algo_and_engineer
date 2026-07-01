# 문제 1.
# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
def discount(price):
    
    if 100000 <= price < 300000:
        return price * 0.95
    elif 300000 <= price < 500000:
        return price * 0.9
    elif 500000 <= price:
        return price * 0.8
    else: return price

def solution(price):
    answer = discount(price)
    
    return int(answer)

# 약간 바보같이 풀어서 다시 정리하면
def discount(price):
    
    if 500000 <= price:
        return price * 0.8
    elif 300000 <= price:
        return price * 0.9
    elif 100000 <= price:
        return price * 0.95
    else: return price

def solution(price):
    answer = discount(price)
    
    return int(answer)

# 더 깔끔한 방법 다시 써봄
def solution(price):
    discount = {500000:0.8, 300000:0.9, 100000:0.95, 0:1}
    
    for discount_price, discount_rate in discount.items():
        if price >= discount_price:
            return int(price * discount_rate)
        
# 문제 2.
# 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(money):
    answer = [money // 5500, money % 5500]
    return answer

# 문제 3.
# 머쓱이는 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 2022년 기준 선생님의 나이 age가 주어질 때, 선생님의 출생 연도를 return 하는 solution 함수를 완성해주세요
def solution(age):
    answer = 2022 - age + 1
    return answer

# 문제 4
# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = []
    
    for i in range(len(num_list)):
        answer.append(num_list[len(num_list) - i - 1])
        
    return answer

# 하지만 왕 쉬운 문법
def solution(num_list):
    return num_list[::-1]

# 문제 5
# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
# 문자열도 배열임을 까먹지마슈...경고유..
def solution(my_string):
    return my_string[::-1]

