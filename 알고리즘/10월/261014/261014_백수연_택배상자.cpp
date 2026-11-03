#include <string>
#include <vector>
#include <deque>

using namespace std;

int solution(vector<int> order) {
    int answer = 0;
    
    int main_belt = 1;
    deque<int> sub_belt;
    
    for (const auto idx : order) {
        
        if (main_belt == idx) {
            main_belt++;
            answer++;
        }
        
        else if (!sub_belt.empty() && sub_belt.back() == idx) {
            sub_belt.pop_back();
            answer++;
        }
        
        else if (main_belt < idx) {
            for (int i = main_belt; i < idx; i++) sub_belt.push_back(i);
            main_belt = idx + 1;
            answer++;
        }
        
        else break;
    }
    
    
    return answer;
}