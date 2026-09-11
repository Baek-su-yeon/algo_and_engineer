#include <iostream>
#include <string>
using namespace std;

/*
유효하지 않은 경우
- 리프 노드에 연산자가 존재
- 리프 노드 아닌 노드에 숫자가 존재

0으로 나누는 경우는 존재하지 않는다고 명시

>> 연산자인지만 확인

리프노드는?
완전이진트리이므로 *2씩 
*/

bool isOperator(string s) {
    return s == "+" || s == "-" || s == "*" || s == "/";
}

int main() {
    for (int tc = 1; tc <= 10; tc++) {
        int N;
        cin >> N;

        int ans = 1;

        for (int i = 0; i < N; i++) {
            int node;
            string value;

            cin >> node >> value;
            // 좌우 자식 노드 존재 여부
            bool hasLeft = node * 2 <= N;
            bool hasRight = node * 2 + 1 <= N;

            if (hasLeft && hasRight) {
                int left, right;
                cin >> left >> right;

                if (!isOperator(value)) {
                    ans = 0;
                }
            }

            else if (hasLeft) {
                int left;
                cin >> left;

                ans = 0;
            }

            else {
                if (isOperator(value)) {
                    ans = 0;
                }
            }
        }

        cout << "#" << tc << " " << ans << '\n';
    }

    return 0;
}