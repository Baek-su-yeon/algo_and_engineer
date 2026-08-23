/*
가장 높은 지점 찾기
현재 지점 기준 상하좌우 값이 현재 값보다 작은지 확인
작다면 반복
작지 않다면 -> 깎은 적 있으면 끝 / 깎은 적 없으면 현재 값 -1로 변경 가능? 
최대 K 만큼만 팔 수 있음.
*/
#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int N, K;
int board[9][9];
bool visited[9][9];
int max_length;
 
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
 
void dfs(int cx, int cy, bool isCut, int length) {
    max_length = max(max_length, length);
 
    for (int i = 0; i < 4; i++) {
        int nx = cx + dx[i];
        int ny = cy + dy[i];
 
        if (nx < 0 || nx >= N || ny < 0 || ny >= N || visited[nx][ny]) continue;
 
        if (board[nx][ny] < board[cx][cy]) {
            visited[nx][ny] = true;
            dfs(nx, ny, isCut, length + 1);
            visited[nx][ny] = false; 
        } else if (!isCut && board[nx][ny] - K < board[cx][cy]) {
            int original_height = board[nx][ny]; 
            visited[nx][ny] = true;
            board[nx][ny] = board[cx][cy] - 1; 
            dfs(nx, ny, true, length + 1);
 
            board[nx][ny] = original_height;
            visited[nx][ny] = false;
        }
    }
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    int T;
    cin >> T;
 
    for (int tc = 1; tc <= T; tc++) {
        cin >> N >> K;
         
        int max_height = 0;
        max_length = 0;
 
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cin >> board[i][j];
                if (board[i][j] > max_height) {
                    max_height = board[i][j];
                }
            }
        }
 
        vector<pair<int, int>> startPoint;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == max_height) {
                    startPoint.push_back({i, j});
                }
            }
        }
 
        for (int i = 0; i < startPoint.size(); i++) {
            pair<int, int> p = startPoint[i];
             
            visited[p.first][p.second] = true;
            dfs(p.first, p.second, false, 1);
            visited[p.first][p.second] = false; 
        }
 
        cout << "#" << tc << " " << max_length << "\n";
    }
 
    return 0;
}