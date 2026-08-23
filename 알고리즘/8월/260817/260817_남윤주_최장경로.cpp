#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
int N, M;
vector<int> graph[11];
bool visited[11];
int answer;
 
void dfs(int cur, int len) {
    answer = max(answer, len);
 
    for (int next : graph[cur]) {
        if (!visited[next]) {
            visited[next] = true;
 
            dfs(next, len + 1);
 
            visited[next] = false;
        }
    }
}
 
int main() {
 
    int T;
    cin >> T;
 
    for (int tc = 1; tc <= T; tc++) {
        cin >> N >> M;
 
        for (int i = 1; i <= N; i++) {
            graph[i].clear();
            visited[i] = false;
        }
 
        for (int i = 0; i < M; i++) {
            int a, b;
            cin >> a >> b;
 
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
 
        answer = 1;
 
        for (int start = 1; start <= N; start++) {
            visited[start] = true;
 
            dfs(start, 1);
 
            visited[start] = false;
        }
 
        cout << "#" << tc << " " << answer << '\n';
    }
 
    return 0;
}
