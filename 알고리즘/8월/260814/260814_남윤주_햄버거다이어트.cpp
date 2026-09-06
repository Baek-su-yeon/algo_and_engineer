/*
햄버거
재료별 점수와 칼로리
정해진 칼로리 이하의 조합 중 최고 점수의 조합을 만들 것.

단순합, 동재료 중복사용 불가

재료별로 점수와 칼로리를 알고 있을 때
여러 개의 재료를 선택하여 제한 칼로리를 넘지 않으며 최대 점수

재귀적으로 i번째 재료를 넣는 경우와 안 넣는 경우

넣었을 때 칼로리가 L 넘으면 패스
*/
#include <iostream>
#include <vector>
using namespace std;

int N, L;
int max_score;
vector<pair<int, int>> ingreds;

// 현재까지 재료 인덱스와 점수, 칼로리를 받아 계산을 이어나감
void calculate(int idx, int cur_score, int cur_calo) {
    if (max_score < cur_score) max_score = cur_score;
    
    if (idx == N) return;
    
    if (cur_calo + ingreds[idx].second <= L) {
        calculate(idx + 1, cur_score + ingreds[idx].first, cur_calo + ingreds[idx].second);
    } 
    
    calculate(idx + 1, cur_score, cur_calo);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;

    string result;

    for (int tc = 1; tc <= T; tc++) {
        // 재료 수, 제한 칼로리
        cin >> N >> L;

        // 최고 점수
        max_score = 0;
        ingreds.clear();

        // N개의 재료 정보
        for (int i = 0; i < N; i++) {
            int score, calo;
            cin >> score >> calo;
            ingreds.push_back({score, calo});
        }
        
        calculate(0, 0, 0);

        result += "#" + to_string(tc) + " " + to_string(max_score) + " \n";
    }
    cout << result;
    return 0;
}