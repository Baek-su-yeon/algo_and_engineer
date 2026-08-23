/*
터널별 생김새
*/
#include<iostream>
#include<queue>
#include<cstring>
 
using namespace std;
 
int N, M, R, C, L;
int board[50][50]; // 터널 구조물 저장
int dist[50][50]; // 해당 위치 도착 시각 저장
 
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};
 
// 터널 구조물 타입 8가지를 4방으로 표현
// 상우하좌
bool pipeDir[8][4] = {
    {0, 0, 0, 0},
    {1, 1, 1, 1},
    {1, 0, 1, 0},
    {0, 1, 0, 1},
    {1, 1, 0, 0},
    {0, 1, 1, 0},
    {0, 0, 1, 1},
    {1, 0, 0, 1}
};
 
int bfs() {
    memset(dist, 0, sizeof(dist));
    queue<pair<int, int>> q;
     
    // 시작점
    q.push({R,C});
    // 도착 시각
    dist[R][C] = 1;
    // 방문 가능 지점
    int ans = 1;
     
    while (!q.empty()) {
        int r = q.front().first;
        int c = q.front().second;
        q.pop();
         
        // 도착 시각이 L이라면 더 이상 이동 X
        if (dist[r][c] == L) {
            continue;
        }
         
        // 터널 타입
        int curType = board[r][c];
        // 상우하좌 연결 여부 확인
        for (int dir = 0; dir < 4; dir++) {
            // 막혀있다면 다음 방향 탐색
            if (!pipeDir[curType][dir]) {
                continue;
            }
             
            int nr = r + dr[dir];
            int nc = c + dc[dir];
             
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) {
                continue;
            }
             
            // 연결 통로 없으면 패스
            if (board[nr][nc] == 0) {
                continue;
            }
            // 방문한 적 있다면 패스
            if (dist[nr][nc] != 0) {
                continue;
            }
             
            int nextType = board[nr][nc];
             
            // 중요!! 다음 칸의 터널도 뚫려있어야 함.
            int opposite = (dir + 2) % 4;
            if (!pipeDir[nextType][opposite]) {
                continue;
            }
            // 도착 시각 기록
            dist[nr][nc] = dist[r][c] + 1;
             
            q.push({nr, nc});
            ans++;
        }
    }
    return ans;
}
int main(int argc, char** argv)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T; 
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        cin >> N >> M >> R >> C >> L;
         
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                cin >> board[r][c];
            }
        }
        int ans = bfs();
        cout << "#" << tc << " " << ans << '\n';
 
    }
    return 0;
}