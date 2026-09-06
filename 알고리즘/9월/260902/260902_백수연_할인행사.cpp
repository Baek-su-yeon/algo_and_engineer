#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    
    unordered_map<string, int> want_count;
    for (int i = 0; i < want.size(); i++)
        want_count[want[i]] = number[i];
    
    unordered_map<string, int> cur_count;
    int match = 0;
    
    auto adjust = [&](const string& item, int delta)
    {
        if (want_count.find(item) == want_count.end()) return;
        
        if (want_count[item] == cur_count[item]) match--;
        
        cur_count[item] += delta;
        
        if (want_count[item] == cur_count[item]) match++;
    };
    
    for (int i = 0; i < 10; i++)
        adjust(discount[i], +1);
    if (match == want.size()) answer++;
    
    for (int start = 1; start <= discount.size() - 10; start++)
    {
        adjust(discount[start - 1], -1);
        adjust(discount[start + 9], +1);
        if(match == want.size()) answer++;
    }
    
    return answer;
}