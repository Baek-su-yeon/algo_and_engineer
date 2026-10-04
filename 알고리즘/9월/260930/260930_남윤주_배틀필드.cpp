#include <iostream>
#include <string>
using namespace std;
 
int H, W;
char board[20][20];
 
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};
char tankShape[4] = {'^', 'v', '<', '>'};
 
int getDir(char ch) {
    if (ch == '^') return 0;
    if (ch == 'v') return 1;
    if (ch == '<') return 2;
    return 3;  // '>'
}
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int T;
    cin >> T;
 
    for (int tc = 1; tc <= T; tc++) {
        cin >> H >> W;
 
        int r = 0, c = 0, dir = 0;
 
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                cin >> board[i][j];
 
                if (board[i][j] == '^' ||
                    board[i][j] == 'v' ||
                    board[i][j] == '<' ||
                    board[i][j] == '>') {
 
                    r = i;
                    c = j;
                     
                    dir = getDir(board[i][j]);
                }
            }
        }
 
        int N;
        string command;
        cin >> N >> command;
 
        for (char cmd : command) {
 
            if (cmd == 'U' || cmd == 'D' || cmd == 'L' || cmd == 'R') {
 
                if (cmd == 'U') dir = 0;
                else if (cmd == 'D') dir = 1;
                else if (cmd == 'L') dir = 2;
                else if (cmd == 'R') dir = 3;
 
                board[r][c] = tankShape[dir];
 
                int nr = r + dr[dir];
                int nc = c + dc[dir];
 
                if (0 <= nr && nr < H &&
                    0 <= nc && nc < W &&
                    board[nr][nc] == '.') {
 
                    board[r][c] = '.';
 
                    r = nr;
                    c = nc;
 
                    board[r][c] = tankShape[dir];
                }
            }
 
            else if (cmd == 'S') {
                int nr = r + dr[dir];
                int nc = c + dc[dir];
 
                while (0 <= nr && nr < H &&
                       0 <= nc && nc < W) {
 
                    if (board[nr][nc] == '*') {
                        board[nr][nc] = '.';
                        break;
                    }
 
                    if (board[nr][nc] == '#') {
                        break;
                    }
 
                    nr += dr[dir];
                    nc += dc[dir];
                }
            }
        }
 
        cout << '#' << tc << ' ';
 
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                cout << board[i][j];
            }
            cout << '\n';
        }
    }
 
    return 0;
}