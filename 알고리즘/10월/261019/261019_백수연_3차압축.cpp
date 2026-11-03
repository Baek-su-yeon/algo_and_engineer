#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;
    
    unordered_map<string, int> dic;
    
    for (char c = 'A'; c <= 'Z'; c++)
        dic[string(1, c)] = c - 'A' + 1;
    
    int next = 27;
    
    for (int i = 0; i < msg.size();) {
        string now = "";
        int value = 0;
        int len = 0;
        
        for (int j = i; j < msg.size(); j++) {
            now += msg[j];
            
            auto it = dic.find(now);
            if (it == dic.end()) {
                dic[now] = next++;
                break;
            }
            
            value = it -> second;
            len++;
            
        }
        
        answer.push_back(value);
        i += len;
    }
    
    return answer;
}