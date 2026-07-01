#include <string>
#include <vector>

using namespace std;
bool visited[200];

void dfs(int current, int n, const vector<vector<int>>& computers) {
    visited[current] = true;
    for (int next = 0; next < n; ++next) {
        if (current != next && computers[current][next] == 1 && !visited[next]) {
            dfs(next, n, computers);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for (int i = 0; i < n; ++i) {
        visited[i] = false;
    }
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            dfs(i, n, computers);
            answer++;
        }
    }
    return answer;
}