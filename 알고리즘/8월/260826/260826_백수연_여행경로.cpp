#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool dfs (string now, const vector<vector<string>>& tickets, map<string, vector<int>>& adj_list, vector<bool>& used, vector<string>& path)
{
    if (path.size() == tickets.size() + 1) return true;
    
    for (const auto& idx : adj_list[now])
    {
        if (used[idx] == false)
        {
            used[idx] = true;
            path.push_back(tickets[idx][1]);
        
            if (dfs(tickets[idx][1], tickets, adj_list, used, path)) return true;
        
            used[idx] = false;
            path.pop_back();
            
        }
    }
    
    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    
    sort(tickets.begin(), tickets.end(),
        [] (const vector<string>& a, const vector<string>& b)
         {
             return a[1] < b[1];
         });
    
    map<string, vector<int>> adj_list;
    vector<bool> used(tickets.size(), false);
    
    for (int i = 0; i < tickets.size(); i++)
    {
        adj_list[tickets[i][0]].push_back(i);
    }
    
    answer.push_back("ICN");
    if (dfs("ICN", tickets, adj_list, used, answer)) return answer;
    else return answer;
}