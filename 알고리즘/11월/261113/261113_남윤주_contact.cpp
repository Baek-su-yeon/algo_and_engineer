#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
 
 
using namespace std;
 
int main() {
    int T = 10;
    for (int tc = 1; tc <= T; tc++) {
        int N, start;
        cin >> N >> start;
 
        vector<vector<int>> connection(101);
        vector<bool> visited(101, false);
 
        for (int i = 0; i < N / 2; i++) {
            int s, e;
            cin >> s >> e;
            connection[s].push_back(e);
        }
 
        queue<int> q;
        q.push(start);
        visited[start] = true;
        int ans;
 
        while (!q.empty()) {
            int size = q.size();
            int max_num = 0;
 
            for (int i = 0; i < size; i++) {
                int now = q.front();
                q.pop();
                max_num = max(max_num, now);
 
                for (int nxt: connection[now]) {
                    if (!visited[nxt]) {
                        visited[nxt] = true;
                        q.push(nxt);
                    }
                }
            }
            ans = max_num;
        }
        cout << "#" << tc << " " << ans << "\n";
         
         
    }
    return 0;
}