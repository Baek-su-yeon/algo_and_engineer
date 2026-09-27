/*
가로 또는 세로 가장 긴 회문의 길이
*/
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// 글자판 고정 크기 100 X 100
const int BOARD_SIZE = 100;

// 회문 판별 함수
// 회문 검사 진행할 문자열 str
// 참조자로 메모리 주소 가져오고, 읽기 전용으로
bool isPalindrome(const string& str, int left, int right) {
    while (left < right) {
        if (str[left] != str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    for (int t = 1; t <= 10; t++) {
        int tc;
        cin >> tc;
        
        vector<string> board(BOARD_SIZE);
        for (int i = 0; i < BOARD_SIZE; i++) {
            cin >> board[i];
        }
        
        int maxLength = 1;
        
        for (int i = 0; i < BOARD_SIZE; ++i) {
            for (int len = BOARD_SIZE; len > maxLength; --len) {
                for (int start = 0; start <= BOARD_SIZE - len; ++start) {
                    if (isPalindrome(board[i], start, start + len - 1)) {
                        maxLength = len;
                        break;
                    }
                }
            }
        }
        
        for (int j = 0; j < BOARD_SIZE; ++j) {
            string colStr = "";
            for (int i = 0; i < BOARD_SIZE; ++i) {
                colStr += board[i][j];
            }
            
            for (int len = BOARD_SIZE; len > maxLength; --len) {
                for (int start = 0; start <= BOARD_SIZE - len; ++start) {
                    if (isPalindrome(colStr, start, start + len - 1)) {
                        maxLength = len;
                        break;
                    }
                }
            }
        }
        cout << "#" << tc << " " << maxLength << "\n";
    }
    return 0;
}