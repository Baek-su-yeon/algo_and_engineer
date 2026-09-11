#include <iostream>
#include <string>
using namespace std;
/*
루트 노드는 1
 
정점이 정수 >> 정점 번호와 양의 정수가
정점이 연산자 >> 정점 번호, 연산자, 왼쪽 자식, 오른쪽 자식의 정점 번호
 
하나의 노드는 값과 왼쪽 자식 번호, 오른쪽 자식 번호 정보를 저장
*/
 
struct Node {
    string value;  
    int left = 0;   
    int right = 0; 
};
 
Node tree[1001];
 
int calculate(int idx) {
 
    // 현재 노드에 들어있는 값
    string value = tree[idx].value;
 
    // 현재 노드가 연산자가 아니라면 숫자 노드
    // 숫자로 변환해서 그대로 반환
    if (value != "+" && value != "-" && value != "*" && value != "/") {
        return stoi(value);
    }
 
    // 연산자 노드라면
    // 왼쪽 서브트리와 오른쪽 서브트리를 먼저 계산
    int leftValue = calculate(tree[idx].left);
    int rightValue = calculate(tree[idx].right);
 
    if (value == "+")
        return leftValue + rightValue;
 
    if (value == "-")
        return leftValue - rightValue;
 
    if (value == "*")
        return leftValue * rightValue;
 
    return leftValue / rightValue;
}
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
     
    for (int tc = 1; tc <= 10; tc++) {
 
        int N;
        cin >> N;
 
        for (int i = 0; i < N; i++) {
 
            int nodeNum;
            string value;
 
            cin >> nodeNum >> value;
 
            tree[nodeNum].value = value;
            tree[nodeNum].left = 0;
            tree[nodeNum].right = 0;
 
            // 연산자 노드라면
            if (value == "+" || value == "-" || value == "*" || value == "/") {
                cin >> tree[nodeNum].left >> tree[nodeNum].right;
            }
        }
 
        int answer = calculate(1);
 
        cout << "#" << tc << " " << answer << '\n';
    }
 
    return 0;
}