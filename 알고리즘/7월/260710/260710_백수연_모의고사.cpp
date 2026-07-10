#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;

    int supo1[5] = {1, 2, 3, 4, 5};
    int supo2[8] = {2, 1, 2, 3, 2, 4, 2, 5};
    int supo3[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    int check[3] = {0,0,0};
    
    for (int i = 0; i < answers.size(); i++)
    {
        if(supo1[i % 5] == answers[i]) check[0] += 1;
        if(supo2[i % 8] == answers[i]) check[1] += 1;
        if(supo3[i % 10] == answers[i]) check[2] += 1;
    }
    
    int max_check = max({check[0], check[1], check[2]});
    
    for (int i = 0; i < 3; i++)
    {
        if (max_check == check[i]) answer.push_back(i + 1);
    }
    
    return answer;
}