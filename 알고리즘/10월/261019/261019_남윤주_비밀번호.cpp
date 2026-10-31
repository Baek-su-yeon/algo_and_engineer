#include <iostream>
#include <list>
#include <string>
#include <iterator>
using namespace std;

int main() {
    for (int tc = 1; tc <= 10; tc++) {
        int N;
        string s;
        cin >> N >> s;

        list<char> nums(s.begin(), s.end());
        // 첫 번째 노드를 가리키는 iterator
        auto it = nums.begin();

        while (it != nums.end()) {
            auto nextIt = next(it);

            if (nextIt != nums.end() && *it == *nextIt) {
                it = nums.erase(it);
                it = nums.erase(it);

                if (it != nums.begin()) {
                    --it;
                }
            }
            else {
                ++it;
            }
        }

        cout << "#" << tc << " ";
        for (char c : nums) {
            cout << c;
        }
        cout << "\n";
    }

    return 0;
}