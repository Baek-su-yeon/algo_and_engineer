#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    stringstream ss(my_string);
    
    string token;
    int sign = 1;
    
    while (ss >> token)
    {
        if (token == "+") sign = 1;
        
        else if (token == "-")sign = -1;
        
        else answer += sign * stoi(token);
    }
    
    return answer;
}