#include <string>
#include <cctype>
#include <map>

using namespace std;

map<string,int> makeSet (const string& str) {
    map<string, int> result;
    
    for (int i = 0; i < str.size() - 1; i++) {
        
        if (!isalpha(str[i]) || !isalpha(str[i + 1])) continue;
        
        string key = {(char)toupper(str[i]), (char)toupper(str[i + 1])};
        
        result[key]++;
    }
    
    return result;
}

int solution(string str1, string str2) {
    
    map<string, int> substr1 = makeSet(str1);
    map<string, int> substr2 = makeSet(str2);
    
    int inter = 0, total1 = 0, total2 = 0;
    for (auto& [k, v] : substr1) {
        total1 += v;
        if (substr2.count(k)) inter += min(v, substr2[k]);
    }
    
    for (auto& [k, v] : substr2) total2 += v;
    
    int uni = total1 + total2 - inter;
    
    if (uni == 0 ) return 65536;
    
    return inter * 65536 / uni;
}