#include <string>
#include <vector>

using namespace std;


int solution(int balls, int share) {
    long long int answer = 1;
    
    share = share < balls - share? share: balls-share;
    
    for (int i = 1; i < share + 1; i++)
    {
        answer = answer * (balls - share + i) / i;
    }
    
    return answer;
}