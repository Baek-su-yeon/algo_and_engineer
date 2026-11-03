#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    string grades[10] = {"A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"};

    for (int tc = 1; tc <= T; tc++) {
        int N, K;
        cin >> N >> K;

        int scores[100];

        int target = 0;

        for (int i = 0; i < N; i++) {
            int mid, final, homework;
            cin >> mid >> final >> homework;
            scores[i] = mid * 35 + final * 45 + homework * 20;

            if (i == K - 1) {
                target = scores[i];
            }
        }
        sort(scores, scores + N, grater<int>());
        for (int i = 0; i < N; i++) {
            if (scores[i] == target) {
                cout << "#" << tc << " " << grades[i / (N / 10)] << "\n";
                break;
            }
        }
    }
    return 0;
}