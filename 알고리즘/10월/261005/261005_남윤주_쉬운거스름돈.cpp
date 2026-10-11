/*
금액단위 큰 것부터 빼면서 계산
*/
#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;

    int money[8] = {50000, 10000, 5000, 1000, 500, 100, 50, 10};

    for (int tc = 1; tc <= T; ++tc) {
        int N; 
        cin >> N;

        cout << "#" << tc << "\n";

        for (int i = 0; i < 8; i++) {
            cout << N / money[i] << " ";
            N %= money[i];
        }
        cout << "\n";
    }
    
    return 0;
}