// 문제1.
// 정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = num1 == num2?1:-1;
    return answer;
}

// 문제 2.
// 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    
    int numer3 = (numer1 * denom2) + (numer2 * denom1);
    int denom3 = denom1 * denom2;
    
    int a = numer3;
    int b = denom3;
    while (b != 0)
    {
        int r = a % b;
        a = b;
        b = r;
    }
    
    answer.push_back(numer3 / a); // 분자 나누기
    answer.push_back(denom3 / a); // 분모 나누기
    return answer;
}