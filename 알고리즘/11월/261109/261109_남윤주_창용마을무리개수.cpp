#include <iostream>
#include <vector>
using namespace std;
 
int parent[101];
 
int find(int x) {
    if (parent[x] == x) {
        return x;
    }
    return parent[x] = find(parent[x]);
}
 
void unin(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
        parent[b] = a;
    }
}
int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int N, M;
        cin >> N >> M;
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }
        for (int i = 0; i < M; i++) {
            int a, b; 
            cin >> a >> b;
            unin(a, b);
        }
        int cnt = 0;
 
        for (int i = 1; i <= N; i++) {
            if (find(i) == i) {
                cnt++;
            }
        }
        cout << "#" << tc << " " << cnt << "\n";
    }
    return 0;
}