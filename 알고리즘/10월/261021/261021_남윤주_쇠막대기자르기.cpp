#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        string problem;
        cin >> problem;

        int ans = 0;
        int opened = 0;

        for (int i = 0; i < problem.size(); i++) {
            if (problem[i] == '(') {
                opened++;
            }
            else {
                opened--;

                if (problem[i - 1] == '(') {
                    ans += opened;
                }
                else {
                    ans++;
                }
            }
        }

        cout << "#" << tc << " " << ans << '\n';
    }

    return 0;
}