// 문제 1
// 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string letter) {
    string answer = "";
    
    for (auto my_letter:my_string)
    {
        if (my_letter == letter[0]) continue;
        answer += my_letter;
    }
    
    return answer;
}

// 문제 2
// 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.
// c++ 슬라이싱 몰랏슴
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers, int num1, int num2) {
    vector<int> answer(numbers.begin() + num1, numbers.begin() + num2 + 1);
    return answer;
}

// 문제 3
// 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.
// PROGRAMMERS-962 행성은 알파벳 소문자만 사용합니다.

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(int age) {
    string answer = "";
    
    unordered_map<char, char> age_in_962 = {
        {'0', 'a'},
        {'1', 'b'},
        {'2', 'c'},
        {'3', 'd'},
        {'4', 'e'},
        {'5', 'f'},
        {'6', 'g'},
        {'7', 'h'},
        {'8', 'i'},
        {'9', 'j'},
    };
    
    for (auto number:to_string(age))
    {
        answer += age_in_962[number];
    }
    
    
    return answer;
}

// 더 깔끔한 풀이
#include <string>
#include <vector>

using namespace std;

string solution(int age) {
    string answer = to_string(age);
    
    for (auto& num:answer) // 참조를 하므로 직접 값을 바꾸게됨
    {
        num += 'a' - '0'; // char형에 영어랑 숫자 코드 차이를 더해주므로 결국 숫자 -> 영문으로 변경
    }
    
    return answer;
}