#include <iostream>
#include <string>
#include <vector>
#include <set>
 
using namespace std;
 
void solve(int tc) {
    int N;
    cin >> N;
     
    // 이름 길이를 인덱스로 하는 vector
    // 중복 제거를 위해 set을 넣어줌
    vector<set<string>> names_by_length(51);
     
    for (int i = 0; i < N; i++) {
        string name;
        cin >> name;
         
        // 이름 넣어줌
        names_by_length[name.length()].insert(name);
    }
    cout << "#" << tc << "\n";
    // 짧은 길이부터 출력
    for (int len = 1; len <= 50; len++) {
        if (!names_by_length[len].empty()) {
            for (const string& name : names_by_length[len]) {
                cout << name << "\n";
            }
        }
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
     
    int T;
    cin >> T;
    for (int tc=1; tc<=T; tc++) {
        solve(tc);
    }
    return 0;
}