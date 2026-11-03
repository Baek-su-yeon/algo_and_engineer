#include <iostream>
#include <algorithm>
 
using namespace std;
 
int main() {
 
    int T; 
    cin >> T;
 
    for (int tc = 1; tc <= T; ++tc) {
        int N; 
        cin >> N;
 
        int corridor[201] = {0};
 
        for (int i = 0; i < N; i++) {
            int a, b;
            cin >> a >> b;
            int start = (min(a, b) + 1)/2;
            int end = (max(a, b) + 1)/2;
 
            for (int j = start; j <= end; j++) {
                corridor[j]++;
            }
        }
        int ans = *max_element(corridor, corridor + 201);
 
        cout << "#" << tc << " " << ans << "\n";
    }
    return 0;
}