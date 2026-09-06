#include <string>
#include <vector>
#include <iostream>
#include <set>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer = {0,0};
    
    set<string> used;
    used.insert(words[0]);
    char last_word = words[0][words[0].size() - 1];
    
    for (int i = 1; i < words.size(); i++)
    {
        if (used.find(words[i]) != used.end() || last_word != words[i][0])
        {
            answer[0] = i % n + 1;
            answer[1] = i / n + 1;
            break;
        }
        
        used.insert(words[i]);
        last_word = words[i][words[i].size() - 1];
    }

    return answer;
}