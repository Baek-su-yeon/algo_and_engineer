#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;

        int a[7][7];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cin >> a[i][j];
            }
        }

        cout << "#" << tc << "\n";

        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {
                cout << a[N - 1 - j][i];
            }

            cout << " ";

            for (int j = 0; j < N; j++) {
                cout << a[N - 1 - i][N - 1 - j];
            }

            cout << " ";

            for (int j = 0; j < N; j++) {
                cout << a[j][N - 1 - i];
            }

            cout << "\n";
        }
    }

    return 0;
}