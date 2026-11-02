#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    const int MOD = 1000000007;

    // dp[y][x]: (x, y)까지 가는 최단경로 개수 (x: 열, 1~m / y: 행, 1~n)
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    vector<vector<bool>> isPuddle(n + 1, vector<bool>(m + 1, false));

    // puddles는 [x, y] 순서이므로 주의
    for (auto& p : puddles) {
        isPuddle[p[1]][p[0]] = true;
    }

    dp[1][1] = 1;

    for (int y = 1; y <= n; y++) {
        for (int x = 1; x <= m; x++) {
            if (y == 1 && x == 1) continue;
            if (isPuddle[y][x]) {
                dp[y][x] = 0;
                continue;
            }
            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD;
        }
    }

    return dp[n][m];
}