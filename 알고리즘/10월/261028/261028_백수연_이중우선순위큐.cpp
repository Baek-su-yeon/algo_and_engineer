#include <string>
#include <vector>
#include <set>
#include <sstream>

using namespace std;

vector<int> solution(vector<string> operations) {
    multiset<int> ms;

    for (const string& op : operations) {
        char cmd;
        int num;
        istringstream iss(op);
        iss >> cmd >> num;

        if (cmd == 'I') {
            ms.insert(num);
        } else if (!ms.empty()) {
            if (num == 1) {
                ms.erase(prev(ms.end()));   // 최댓값 하나만 삭제
            } else {
                ms.erase(ms.begin());       // 최솟값 하나만 삭제
            }
        }
    }

    if (ms.empty()) return {0, 0};
    
    return {*ms.rbegin(), *ms.begin()};
}