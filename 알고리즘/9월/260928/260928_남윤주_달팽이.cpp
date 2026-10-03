#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    
    int dr[4] = {0, 1, 0, -1};
    int dc[4] = {1, 0, -1, 0};
    
    for (int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;
        
        int arr[10][10] = {0};
        int r = 0;
        int c = 0;
        int dir = 0;
        
        for (int num = 1; num <= N * N; num++) {
            arr[r][c] = num;
            
            int nr = r + dr[dir];
            int nc = c + dc[dir];
            
            if (nr < 0 || nr >= N || nc < 0 || nc >= N || arr[nr][nc] != 0) {
                dir = (dir + 1) % 4;
                nr = r + dr[dir];
                nc = c + dc[dir];
            }
            r = nr;
            c = nc;
        }
        cout << "#" << tc << "\n";
        
        for (int i = 0; i <N; i++) {
            for (int j = 0; j < N; j++) {
                cout << arr[i][j];
                if (j != N-1) {
                    cout << " ";
                }
            }
            cout << "\n";
        }
    }
    return 0;
}