#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    unordered_map<string, int> count;
    string snum;
    
    for (const auto& sub : s)
    {
        if (sub == '{' || sub == '}') continue;
        
        if (sub == ',')
        {   
            count[snum]++;
            snum = "";
        }
        else snum += sub;
    }
       
    count[snum]++;
    
    vector<pair<string, int>> vcount(count.begin(), count.end());
    
    sort(vcount.begin(), vcount.end(), [](const auto& a, const auto& b) {
        return a.second > b.second;
    });
    
    for (int i = 0; i < vcount.size(); i++)
        answer.push_back(stoi(vcount[i].first));
    
    return answer;
}