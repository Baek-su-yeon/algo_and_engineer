#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;

    for (const string& tree : skill_trees) {
        string filtered = "";
        for (char c : tree) {
            if (skill.find(c) != string::npos) {
                filtered += c;
            }
        }

        if (skill.compare(0, filtered.size(), filtered) == 0) {
            answer++;
        }
    }

    return answer;
}