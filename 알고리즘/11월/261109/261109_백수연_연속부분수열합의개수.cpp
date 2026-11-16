#include <vector>
#include <set>

using namespace std;

int solution(vector<int> elements) {
    int n = elements.size();
    set<int> sums;

    for (int start = 0; start < n; start++) {
        int sum = 0;
        for (int len = 0; len < n; len++) {
            sum += elements[(start + len) % n];
            sums.insert(sum);
        }
    }
    return sums.size();
}