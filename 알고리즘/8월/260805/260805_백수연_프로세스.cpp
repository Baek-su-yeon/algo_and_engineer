#include <string>
#include <vector>
#include <deque>
#include <utility>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    
    deque<pair<int, int>> queue;
    
    for (int i = 0; i < priorities.size(); i++)
        queue.push_back({priorities[i],i});
    
    sort(priorities.begin(), priorities.end(), greater<int>());
        
    int idx = 0;
    
    while (!queue.empty())
    {
        int now_priorities = priorities[idx];
        
        pair<int, int> now_process = queue[0];
        
        if (now_priorities != now_process.first)
        {
            queue.pop_front();
            queue.push_back(now_process);
        }
        
        else
        {
            if (now_process.second == location)
            {
                return idx + 1;
            }
            idx++;
            queue.pop_front();
        }
    }
    
    return answer;
}