#include <string>
#include <vector>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    
    for (auto letter : my_string)
    {
        if (47 < letter && letter < 58) answer += letter - '0';
    }
    
    return answer;
}