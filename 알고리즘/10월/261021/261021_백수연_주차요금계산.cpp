#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    map<string, int> inTime;   
    map<string, int> total;   

    for (const string& rec : records) {
        istringstream iss(rec);
        string time, car, type;
        iss >> time >> car >> type;

        int minute = stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3, 2));

        if (type == "IN") {
            inTime[car] = minute;
        } else {
            total[car] += minute - inTime[car];
            inTime.erase(car);
        }
    }

    const int END = 23 * 60 + 59;
    for (auto& [car, t] : inTime) {
        total[car] += END - t;
    }

    vector<int> answer;
    for (auto& [car, t] : total) {
        int fee = fees[1];
        if (t > fees[0]) {
            fee += (int)ceil((double)(t - fees[0]) / fees[2]) * fees[3];
        }
        answer.push_back(fee);
    }
    return answer;
}