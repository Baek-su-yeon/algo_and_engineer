#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    
    int top = 0;
    
    while (top < progresses.size())
    {
        int count = 0;
        int day = (99 - progresses[top]) / speeds[top] + 1;
        
        for (int i = top; i < progresses.size(); i++)
        {
            int progress = progresses[i] + (speeds[i] * day);
            
            if (100 <= progress) count++;
            else break;
        }
        
        answer.push_back(count);
        top += count;
        
    }
    
    return answer;
}