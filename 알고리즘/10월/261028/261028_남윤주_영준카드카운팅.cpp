/*
카드문자열을 입력받고
3개씩 끊어서 확인
겹치는 것 하나라도 발견 시 ERROR 출력하고 종료
그 외에는 무늬 별로 관리
 
무늬별로 관리
*/
 
#include <iostream>
#include <string>
using namespace std;
 
int main() {
    int T;
    cin >> T;
 
    for (int tc = 1; tc <= T; tc++) {
        string s;
        cin >> s;
 
        // 네 가지 무늬, 0부터 13
        bool cards[4][14] = {false};
        // 카드 개수만 카운트
        int cnt[4] = {0};
        bool error = false;
 
        for (int i = 0; i < s.size(); i += 3) {
            // 무늬 종류
            char type = s[i];
            int num = (s[i + 1] - '0') * 10 + (s[i + 2] - '0');
 
            int idx;
            if (type == 'S') idx = 0;
            else if (type == 'D') idx = 1;
            else if (type == 'H') idx = 2;
            else idx = 3;
 
            if (cards[idx][num]) {
                error = true;
                break;
            }
 
            cards[idx][num] = true;
            cnt[idx]++;
        }
 
        cout << "#" << tc << " ";
 
        if (error) {
            cout << "ERROR\n";
        } else {
            for (int i = 0; i < 4; i++) {
                if (i > 0) cout << " ";
                cout << 13 - cnt[i];
            }
            cout << "\n";
        }
    }
 
    return 0;
}