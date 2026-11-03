/*
8개의 숫자
앞에서부터 1~5까지 감소시키고 뒤로 보내기를 반복.
0보다 작아지는 경우 발생 시 해당 숫자는 0으로 하고 맨 뒤로 보내고 종료

마지막 암호 배열은 모두 한 자리 수 >> 8개의 숫자들이 비슷한 값

총 8사이클을 돌면 모든 수가 15 감소되고 숫자 배열 순서도 돌아옴

젤 작은 숫자 15로 나눈 몫 구해서 몫 * 15만큼 모든 수에서 빼고
시뮬레이션
*/
#include <iostream>
using namespace std;

int main() {
    int T = 10;
    for ( int tc = 1; tc <= T; tc++) {
        int a;
        cin >> a;
        
        int nums[8] = {};
        int smallest = 2e9;
        for (int i = 0; i < 8; i++) {
            cin >> nums[i];
            if (smallest > nums[i]) {
                smallest = nums[i];
            }
        }
        int cnt = smallest / 15 - 1;
        int common = cnt * 15;
        
        for (int i = 0; i < 8; i++) {
            nums[i] -= common;
        }
        
        
        int head = 0;
        int minus = 0;
        
        while (true) {
            
            nums[head] -= (minus%5 + 1);
            minus++;
            if (nums[head] <= 0) {
                nums[head] = 0;
                head++;
                head %= 8;
                break;
            }
            head++;
            head %= 8;
        }
        
        cout << "#" << tc <<" ";
        for (int idx = 0; idx < 8; idx++) {
            cout << nums[(head+idx) % 8] << " ";
        }
        cout << "\n";
    
    }
    return 0;
}