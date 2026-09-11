#include <iostream>
using namespace std;
/*
중위순회
왼쪽 현재 오른쪽
*/
 
char tree[101];
int leftChild[101];
int rightChild[101];
 
void inorder(int node) {
    if (node == 0) {
        return;
    }
    // 왼쪽 방문. 재귀적으로 깊이 우선 > 중간 > 오른쪽
    inorder(leftChild[node]);
    cout << tree[node];
    inorder(rightChild[node]);
}
 
 
int main()
{
 
    for (int tc = 1; tc <= 10; tc++)
    {
        int N;
        cin >> N;
        // 초기화
        for (int i = 1; i <= N; i++)
        {
            leftChild[i] = 0;
            rightChild[i] = 0;
        }
 
        for (int i = 0; i < N; i++)
        {
            int node;
            char value;
 
            cin >> node >> value;
 
            tree[node] = value;
 
            if (node * 2 <= N)
                leftChild[node] = node * 2;
 
            if (node * 2 + 1 <= N)
                rightChild[node] = node * 2 + 1;
 
            int dummy;
 
            if (node * 2 <= N)
                cin >> dummy;
 
            if (node * 2 + 1 <= N)
                cin >> dummy;
        }
 
        cout << "#" << tc << " ";
        inorder(1);
 
        cout << '\n';
    }
 
    return 0;
}