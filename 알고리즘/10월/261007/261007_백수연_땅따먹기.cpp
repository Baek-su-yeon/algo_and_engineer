#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> land) {
    for (int i = 1; i < land.size(); i++) {
        for (int j = 0; j < 4; j++) {
            int best = 0;
            for (int k = 0; k < 4; k++)
                if (k != j) best = max(best, land[i-1][k]);
            land[i][j] += best;
        }
    }
    return *max_element(land.back().begin(), land.back().end());
}