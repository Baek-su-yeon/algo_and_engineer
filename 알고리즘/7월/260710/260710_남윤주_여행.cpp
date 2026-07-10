#include <iostream>
#include <string>

using namespace std;

void solve(int tc) {
    string s;
    cin >> s; 

    bool hasN = false, hasS = false, hasE = false, hasW = false;

    for (char c : s) {
        if (c == 'N') hasN = true;
        else if (c == 'S') hasS = true;
        else if (c == 'E') hasE = true;
        else if (c == 'W') hasW = true;
    }

    if ((hasN == hasS) && (hasE == hasW)) {
        cout <<"Yes\n";
    } else {
        cout <<"No\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        solve(tc);
    }

    return 0;
}