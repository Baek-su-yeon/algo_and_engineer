#include <string>
#include <vector>
#include <queue>

using namespace std;

long long NowTired (priority_queue<int>& queue) {
    long long result = 0;
    
    while(!queue.empty()) {
        long long top = queue.top();
        result += top * top;
        queue.pop();
    }
    
    return result;
}

long long solution(int n, vector<int> works) {
    long long answer = 0;
    
    priority_queue<int> pq;
    for (const auto work : works)
        pq.push(work);
    
    while (0 < n && !pq.empty()) {
        int top = pq.top();
        if (top == 0) break;
        
        pq.pop();
        
        pq.push(top - 1);
        n--;
    }
    
    answer = NowTired(pq);
    
    return answer;
}