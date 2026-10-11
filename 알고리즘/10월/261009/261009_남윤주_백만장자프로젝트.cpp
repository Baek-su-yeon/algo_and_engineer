
/*
아이디어
1. 미래의 최고 판매 가격을 기준으로 이익을 계산한다.
2. 배열을 뒤에서부터 탐색하며 최대 가격을 갱신한다.
3. 현재 가격이 최대 가격보다 낮으면 구매 후 판매한다고 가정한다.
4. (최대 가격 - 현재 가격)을 누적하여 최대 이익을 구한다.
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;

        vector<int> price(N);

        for (int i = 0; i < N; i++) {
            cin >> price[i];
        }

        int maxPrice = 0;
        long long profit = 0;

        for (int i = N - 1; i >= 0; i--) {
            maxPrice = max(maxPrice, price[i]);
            profit += maxPrice - price[i];
        }

        cout << "#" << tc << " " << profit << "\n";
    }

    return 0;
}
