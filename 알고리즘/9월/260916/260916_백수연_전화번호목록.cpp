#include <string>
#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

bool solution(vector<string> phone_book) {
    
    unordered_set<string> numbers;
    
    for (const auto& number:phone_book)
        numbers.insert(number);
    
    for (const auto& number:phone_book)
    {
        for (int i = 1; i < number.size(); i++)
        {
            string target = number.substr(0, i);
            if (numbers.find(target) != numbers.end())
            {
                return false;
            }
        }
    }
    
    return true;
}