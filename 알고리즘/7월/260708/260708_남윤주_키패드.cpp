#include <string>
#include <vector>
#include <cmath>

using namespace std;

pair<int, int> keypad[12] = {
    {3, 1}, // 0
    {0, 0}, {0, 1}, {0, 2}, 
    {1, 0}, {1, 1}, {1, 2}, 
    {2, 0}, {2, 1}, {2, 2}, 
    {3, 0},         {3, 2}  
};

string solution(vector<int> numbers, string hand) {
    string answer = "";
    
    int left_pos = 10;
    int right_pos = 11;
    
    for (int num : numbers) {
        if (num == 1 || num == 4 || num == 7) {
            answer += "L";
            left_pos = num;
        } 
        else if (num == 3 || num == 6 || num == 9) {
            answer += "R";
            right_pos = num;
        } 
        else { 
            int left_dist = abs(keypad[left_pos].first - keypad[num].first) + abs(keypad[left_pos].second - keypad[num].second);
            int right_dist = abs(keypad[right_pos].first - keypad[num].first) + abs(keypad[right_pos].second - keypad[num].second);
            
            if (left_dist < right_dist) {
                answer += "L";
                left_pos = num;
            } 
            else if (right_dist < left_dist) {
                answer += "R";
                right_pos = num;
            } 
            else { 
                if (hand == "left") {
                    answer += "L";
                    left_pos = num;
                } else {
                    answer += "R";
                    right_pos = num;
                }
            }
        }
    }
    
    return answer;
}