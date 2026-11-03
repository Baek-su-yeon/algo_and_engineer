#include <string>
#include <vector>

using namespace std;

int TopDown (vector<vector<int>>& triangle) {

    for (int i = 1; i < triangle.size(); i++) {
        for (int j = 0; j < triangle[i].size(); j++) {
            
            if (j == 0) {
                triangle[i][j] += triangle[i - 1][j];
            }
            else if (j == triangle[i].size() - 1) {
                triangle[i][j] += triangle[i - 1][j - 1];
            }
            else {
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1]);
            }
        }
    }
    
    int answer = 0;
    for (int i = 0; i < triangle[triangle.size() - 1].size(); i++)
        answer = max(answer, triangle[triangle.size() - 1][i]);

    return answer;
}

int BottomUp (vector<vector<int>>& triangle) {
    
    for (int i = triangle.size() - 2; 0 <= i; i--) {
        for (int j = 0; j < triangle[i].size(); j++) {
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1]);
        }
    }
    
    int answer = triangle[0][0];

    return answer;
}

int solution(vector<vector<int>> triangle) {
    
    // int answer = TopDown(triangle);
    int answer = BottomUp(triangle);
    
    return answer;
}