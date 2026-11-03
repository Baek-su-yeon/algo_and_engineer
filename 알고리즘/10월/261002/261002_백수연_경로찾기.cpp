#include <string>
#include <vector>

using namespace std;

struct Point {
    int x;
    int y;
};

int solution(string dirs) {
    int answer = 0;    
    
    vector<vector<int>> visited(21, vector<int> (21, 0));
    
    Point now = {10, 10};
    Point d = {0, 0};
    for (const auto& dir : dirs)
    {
        if (dir == 'U') d = {-1, 0};
        else if (dir == 'D') d = {1, 0};
        else if (dir == 'L') d = {0, -1};
        else d = {0, 1};
        
        Point next = {now.x + d.x, now.y + d.y};
        
        if (next.x < 0 || 20 < next.x || next.y < 0 || 20 < next.y) continue;
        
        if (visited[next.x][next.y] == 0) answer++;
        
        visited[next.x][next.y] = 1;
        now = {now.x + (d.x * 2), now.y + (d.y * 2)};
    }
    
    return answer;
}