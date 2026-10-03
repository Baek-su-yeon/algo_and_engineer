#include <string>
#include <vector>

using namespace std;

void find_word(const string& word, const string& vowel, string now, int& count, bool& find)
{
    for (int i = 0; i < vowel.size(); i++)
    {
        string next = now + vowel[i];
        count++;

        if (next == word)
        {
            find = true;
            return;
        }

        if (next.size() < 5)
        {
            find_word(word, vowel, next, count, find);

            if (find) return; // 없으면 숫자 계속 증가
        }
    }

    return;
}

int solution(string word) {
    int answer = 0;
    bool find = false;
    
    find_word(word, "AEIOU", "", answer, find);
    
    return answer;
}