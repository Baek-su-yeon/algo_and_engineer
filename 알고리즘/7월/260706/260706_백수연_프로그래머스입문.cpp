// 문제 1
// 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> numbers, string direction) {
    vector<int> answer;

    if (direction == "right")
    {
        int temp = numbers.back();
        numbers.pop_back();
        numbers.insert(numbers.begin(), temp);
    }
    else
    {
        int temp = numbers.front();
        numbers.erase(numbers.begin());
        numbers.push_back(temp);
    }
    
    return answer = numbers;
}

// 함수 쓴거
// rotate(시작위치, 새로운_첫번째가_될_위치, 끝위치);
// 주의할 것: vector.end()는 마지막 원소 다음 위치를 가리킴
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers, string direction) {
    vector<int> answer;
    
    if (direction == "right")
    {
        rotate(numbers.begin(), numbers.end() - 1, numbers.end());
    }
    else
    {
        rotate(numbers.begin(), numbers.begin() + 1, numbers.end());
    }
    
    
    return answer = numbers;
}