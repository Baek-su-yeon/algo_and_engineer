#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer(numbers.size(), -1);
    vector<int> idxs;
    
    for (int i = 0; i < numbers.size(); i++)
    {
        while(!idxs.empty() && numbers[idxs.back()] < numbers[i])
        {
            answer[idxs.back()] = numbers[i];
            idxs.pop_back();
        }
        idxs.push_back(i);
    }
    
    return answer;
}