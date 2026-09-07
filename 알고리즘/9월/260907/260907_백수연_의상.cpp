#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    
    unordered_map<string, int> types;
    
    for (auto cloth : clothes)
        types[cloth[1]]++;
    
    for (const auto& [key, value] : types)
        answer *= value + 1;
    
    return answer - 1;
}