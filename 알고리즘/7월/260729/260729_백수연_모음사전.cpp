#include <string>
#include <vector>

using namespace std;

int find_dictionary(string word, string vowels, string now, int& count)
{
    
    for (int i = 0; i < vowels.size(); i++)
    {
        string next = now + vowels[i];
        
        count++;
        
        if (next == word) return count;
        
        if (next.size() < 5)
        {
            int result = find_dictionary(word, vowels, next, count);
            
            if (result != -1) return result;
        }
    }
    
    return -1;
    
}

int solution(string word) {
    int answer = 0;
    int count = 0;
    string vowels = "AEIOU";
    
    answer = find_dictionary(word, vowels, "", count);
    
    return answer;
}