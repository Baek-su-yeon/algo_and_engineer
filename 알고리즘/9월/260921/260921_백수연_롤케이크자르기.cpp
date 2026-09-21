#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<int> topping) {
    int answer = 0;
    
    unordered_map<int, int> left;
    unordered_map<int, int> right;
    
    // 제일 처음 맨 앞을 자르는 경우
    int rtopping = 0;
    for (int i = 0; i < topping.size(); i++)
    {
        right[topping[i]]++;
        if (right[topping[i]] == 1) rtopping++;
    }
    
    // 1번째부터 topping.size() 만큼 오른쪽으로 1칸씩 이동
    int ltopping = 0;
    for (int i = 1; i < topping.size(); i++)
    {
        left[topping[i - 1]]++;
        right[topping[i - 1]]--;
        
        if (left[topping[i - 1]] == 1) ltopping++;
        if (right[topping[i - 1]] == 0) rtopping--;
        if (ltopping == rtopping) answer++;
    }
    
    return answer;
}