#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array) {
    vector<int> answer;
    
    int maxIdx = max_element(array.begin(), array.end()) - array.begin();
    
    answer.push_back(array[maxIdx]);
    answer.push_back(maxIdx);
    
    return answer;
}