#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    
    for (int tc = 1; tc <= T; ++tc) {
        int K;
        string s;
        
        cin >> K;
        cin >> s;
        
        // 접두어들을 vector로 관리
        vector<string> suffix;
        
        for (int i = 0; i < s.size(); ++i) {
            suffix.push_back(s.substr(i));
        }
        
        sort(suffix.begin(), suffix.end());
        
        cout << "#" << tc << " ";
        
        if (K > suffix.size()) {
            cout << "none";
        } else {
            cout << suffix[K - 1];
        }
        
        cout << "\n";
        
    }
    return 0;
}
        