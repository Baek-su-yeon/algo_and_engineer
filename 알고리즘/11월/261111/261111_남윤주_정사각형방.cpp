#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
/*
N N 방
모든 방에 서로 다른 숫자
상하좌우 이동 가능
현재 방 숫자 + 1인 경우에만 이동 가능
 
가장 많은 개수의 방을 이동할 수 있는
처음 시작 위치 찾기
*/
int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int N;
        cin >> N;
        int M = N * N;
 
        vector<int> row(M+2), col(M+2);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int num;
                cin >> num;
                row[num] = i;
                col[num] = j;
            }
        }
         
        int bestStart = 1, bestLen = 1;
        int curStart = 1, curLen = 1;
 
        for (int num = 2; num <= M; num++) {
            int dist = abs(row[num] - row[num-1]) + abs(col[num] - col[num-1]);
            if (dist == 1) {
                curLen++;
            } else {
                curStart = num;
                curLen = 1;
            }
            if (curLen > bestLen) {
                bestLen = curLen;
                bestStart = curStart;
            }
        }
        cout << "#" << tc << " " << bestStart << " " << bestLen << "\n";
    }
    return 0;
}