#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int solution(int n, int w, int num) {

    auto get_coords = [w](int box) {
        int r = (box - 1) / w; 
        int c = (box - 1) % w; 
        
       
        if (r % 2 == 1) {
            c = w - 1 - c;
        }
        return make_pair(r, c);
    };

    auto target_pos = get_coords(num);
    int target_r = target_pos.first;
    int target_c = target_pos.second;

    auto last_pos = get_coords(n);
    int last_r = last_pos.first;
    int last_c = last_pos.second;

    int total_layers = last_r - target_r + 1;

    if (last_r % 2 == 0) {
        if (target_c > last_c) {
            total_layers--;
        }
    } 
    else {
        if (target_c < last_c) {
            total_layers--;
        }
    }

    return total_layers;
}