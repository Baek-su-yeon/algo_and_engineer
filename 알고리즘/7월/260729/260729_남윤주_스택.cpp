#include <iostream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

int main() {

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int n;
        cin >> n;
       // 출력 숫자 순서
        vector<int> sequence(n);

        for (int& number : sequence) {
            cin >> number;
        }

        stack<int> numbers;
        string result;
        result.reserve(2 * n);

        int nextNumber = 1;
        bool possible = true;

        for (int target : sequence) {
            // 스택 속 숫자 확인
            // 타겟이 아니면 스택에 다음 숫자를 넣음
            while (nextNumber <= n &&
                   (numbers.empty() || numbers.top() != target)) {
                numbers.push(nextNumber++);
                result += '+';
            }
            // 타겟 숫자라면 뺌
            // 타겟 숫자가 아닌데 숫자가 남아있다면 실패
            if (!numbers.empty() && numbers.top() == target) {
                numbers.pop();
                result += '-';
            } else {
                possible = false;
                break;
            }
        }

        cout << '#' << tc<< ' ';

        if (possible) {
            cout << result << '\n';
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}