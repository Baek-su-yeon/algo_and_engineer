#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// int solution(int k, vector<vector<int>> dungeons) {
//     int answer = 0;
    
//     sort(dungeons.begin(), dungeons.end());
    
//     do {
        
//         int user = k;
//         int count = 0;
        
//         for (const auto& dungeon : dungeons)
//         {
//             if (user < dungeon[0])
//             {
//                 answer = max(answer, count);
//                 break;
//             }
            
//             user -= dungeon[1];
//             count++;
//         }
        
//         answer = max(answer, count);
        
//     } while(next_permutation(dungeons.begin(), dungeons.end()));
    
//     return answer;
// }

void permutation (const vector<vector<int>>& dungeons, int k, vector<int>& path, vector<bool>& used, int& answer)
{
    if (path.size() == dungeons.size())
    {
        int count = 0;
        int user = k;
        
        for (const auto& idx : path)
        {
            if (user < dungeons[idx][0])
            {
                answer = max(answer, count);
                break;
            }
            
            user -= dungeons[idx][1];
            count++;
        }
        
        answer = max(answer, count);
        
        return;
    }
    
    for (int i = 0; i < dungeons.size(); i++)
    {
        if (!used[i])
        {
            used[i] = true;
            path.push_back(i);
            
            permutation(dungeons, k, path, used, answer);
            
            path.pop_back();
            used[i] = false;
        }
    }
    
    return;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = 0;
    vector<int> path;
    vector<bool> used (dungeons.size(), false);
    
    permutation(dungeons, k, path, used, answer);
    
    return answer;
}