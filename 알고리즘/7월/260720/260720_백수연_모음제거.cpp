#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    string vowels = "aeiou";
    
    for (auto letter : my_string)
    {
        if(vowels.find(letter) == std::string::npos) answer += letter;
    }
    
    return answer;
}