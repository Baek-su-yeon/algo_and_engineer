// 2중 for문
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size(), 0);
    
    for (int i = 0; i < prices.size() - 1; i++)
    {
        int now = prices[i];
        
        for (int j = i + 1; j < prices.size(); j++)
        {
            answer[i]++;
            
            int next = prices[j];
            if (next < now) break;
        }
    }
    
    return answer;
}

// 스택
#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size(), 0);
    stack<int> st;
    
    for (int i = 0; i < prices.size(); i++)
    {
        int now_price = prices[i];
        
        while(!st.empty() && now_price < prices[st.top()])
        {
            int idx = st.top();
            st.pop();
            
            int time = i - idx;
            answer[idx] = time;
        }
        
        st.push(i);
    }
    
    while(!st.empty())
    {
        int idx = st.top();
        st.pop();
        
        int time = (prices.size() - 1) - idx;
        answer[idx] = time;
        
    }
    
    return answer;
}