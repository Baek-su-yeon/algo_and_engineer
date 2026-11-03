#include <string>
#include <algorithm>
using namespace std;

string toBase(int num, int n) {
    if (num == 0) return "0";
    string digits = "0123456789ABCDEF", s;
    while (num > 0) {
        s += digits[num % n];
        num /= n;
    }
    reverse(s.begin(), s.end());
    return s;
}

string solution(int n, int t, int m, int p) {
    string all;
    for (int num = 0; all.size() < t * m; num++)
        all += toBase(num, n);

    string answer;
    for (int i = p - 1; answer.size() < t; i += m)
        answer += all[i];
    return answer;
}