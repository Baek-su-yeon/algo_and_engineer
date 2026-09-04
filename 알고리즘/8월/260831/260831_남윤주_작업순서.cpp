#include <iostream>
#include <vector>
#include <queue>
using namespace std;
 
// 작업에 선행관계가 존재
// 정점 V개, 간선 E개
/*
한 작업이 수행되기 위해서는 선행작업이 모두 처리된 상태여야 함.
각 작업별로 선행 필요한 작업 개수
작업 완료 여부를 관
 
*/
int main() {
    int T = 10;
    for (int tc = 1; tc <= T; tc++) {
        int V, E;
        cin >> V >> E;
         
        vector<vector<int>> graph(V+1);
        vector<int> indegree(V+1, 0);
         
        for (int i = 0; i < E; i++) {
            int startNode, endNode;
            cin >> startNode >> endNode;
            graph[startNode].push_back(endNode);
            indegree[endNode]++;
        }
 
        // 선행작업 없는 정점부터
        queue<int> q;
 
        for (int i = 1; i <= V; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
 
        cout << "#" << tc << " ";
 
        while (!q.empty()) {
            int current = q.front();
            q.pop();
 
            cout << current << " ";
 
            // 선행작업이 수행된 정점
            for (int nxt : graph[current]) {
                indegree[nxt]--;
                if (indegree[nxt] == 0) {
                    q.push(nxt);
                }
            }
        }
         
        cout << "\n";
    }
    return 0;
}