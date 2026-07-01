// 문제 1.
// 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
// 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
#include <string>
#include <vector>

using namespace std;

int solution(int price) {
    int answer = price;
    
    if (500000 <= price) return answer * 0.8;
    else if (300000 <= price) return answer * 0.9;
    else if (100000 <= price) return answer * 0.95;
    
    return answer;
}

// 문제 2.
// 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int money) {
    vector<int> answer;
    
    answer.push_back(money / 5500);
    answer.push_back(money % 5500);
    
    return answer;
}

// 깔끔버전
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int money) {
    vector<int> answer = {money / 5500, money % 5500};
    
    return answer;
}

// 문제 3
// 머쓱이는 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 2022년 기준 선생님의 나이 age가 주어질 때, 선생님의 출생 연도를 return 하는 solution 함수를 완성해주세요
#include <string>
#include <vector>

using namespace std;

int solution(int age) {
    int answer = 2022 - age + 1;
    return answer;
}

// 문제 4
// 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    
    for (int i = num_list.size() - 1; -1 < i ; i--)
    {
        answer.push_back(num_list[i]);
    }
    
    return answer;
}

// 라이브러리 쓴거
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> num_list) {
    
    reverse(num_list.begin(), num_list.end());
    
    return num_list;
}

// 문제 5
// 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string) {
    
    string new_my_string(my_string.rbegin(), my_string.rend()); // 원래 배열 값 변경 X, 뒤에서부터 읽어서 새로운 배열을 만듦
    
    // reverse(my_string.begin(), my_string.end()); // 원래 배열 값 변경 O
    
    // return my_string;
    return new_my_string;
    
}

// 문제 6... 어엥 이제 너무 기초는 c++로 하고 넘길 것
// 참고로 파이썬은 걍 문자열에 * 개수 하면 끗임~
#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    
    for (int i = 1; i < n + 1; i++)
    {
        // cout << string(i,'*') << endl; 이렇게하면 이중 for문 필요 없이 바로 가능
        for (int j = 0; j < i; j++) cout << "*";
        cout << endl;
    }
    return 0;
}

// 문제 7
// 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer = {0, 0};
    // vector<int> answer(2, 0); vector 초기화 방식 외우도록
    
    for (int i = 0; i < num_list.size(); i++)
    {
        if (num_list[i] % 2 == 0) answer[0] += 1;
        else answer[1] += 1;
    }
    
    return answer;
}

// 문제 8
// 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {
    string answer = "";
    
    for (char my_char:my_string) answer += string(n, my_char);
    
    return answer;
}