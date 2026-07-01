// 문제 1.
// 정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = num1 + num2;
    return answer;
}

// 문제 2.
// 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = num1 - num2;
    return answer;
}

// 문제 3.
// 정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = num1 * num2;
    return answer;
}

// 문제 4.
// 정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = num1 / num2;
    return answer;
}

// 문제 5.
// 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 solution 함수를 완성해주세요.
// 형변환 방식, 나눗셈 결과 잘 이해할 것
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = (double)num1 / num2 * 1000;
    return answer;
}