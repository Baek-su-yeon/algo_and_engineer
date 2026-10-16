#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

bool check (long long num) {
    
    if (num < 2) return false;
    
    for (long long i = 2; i <= pow(num, 0.5); i++) {
        if (num % i == 0) return false;
    }
    
    // for (long long i = 2; i < num / 2; i++) {
    //     if (num % i == 0) return false;
    // }
    
    return true;
}


int solution(int n, int k) {
    int answer = 0;
    
    string base;
    // 거꾸로 읽어야함
    while (0 < n) {
        base += to_string(n % k);
        n /= k;
    }
    
    reverse(base.begin(), base.end());
    
    int prev = 0;
    for (int i = 0; i < base.size(); i++) {
        
        if (base[i] == '0') {
            long long sub = stoll(base.substr(prev, i - prev));
            if (check(sub)) answer++;
            prev = i;
        }
        
    }
    
    // 남은 것 처리
    if (check(stoll(base.substr(prev)))) answer++;
    
    return answer;
}