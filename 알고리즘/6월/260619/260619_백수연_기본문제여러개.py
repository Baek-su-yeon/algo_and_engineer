# 문제1.
# 정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    answer = 0
    
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer

# 문제2.
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    numer3 = (numer1 * denom2) + (numer2 * denom1)
    denom3 = denom1 * denom2
    
    a, b = numer3, denom3
    while b != 0:
        a, b = b, a % b
    
    # 최대공약수
    gcd_value = a
            
    return [numer3 // gcd_value, denom3 // gcd_value]