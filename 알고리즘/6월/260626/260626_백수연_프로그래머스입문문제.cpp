// 문제 1.
// 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    
    for (int i = 0; i < n + 1; i++)
    {
        if (i % 2 != 0) answer.push_back(i);
    }
    
    return answer;
}

// 문제 2.
// 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    
    if (n % 7 == 0) answer = n / 7;
    else answer = n / 7 + 1;
    
    return answer;
}

// 문제 3.
// 머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
#include <string>
#include <vector>
#include <numeric>

using namespace std;

int my_gcd (int n, int num)
{
    while (num != 0)
    {
        int temp = n % num;
        n = num;
        num = temp;
    }
    
    return n;
}

int solution(int n) {
    int answer = n / my_gcd(n, 6);
    
    answer = n / gcd(n, 6);
    
    return answer;
}

// 문제 4.
// 머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다. 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
#include <string>
#include <vector>

using namespace std;


int solution(int slice, int n) {
    int answer = 0;
    
    if (n % slice != 0) answer = n / slice + 1;
    else answer = n / slice;
    
    return answer;
}

// 문제 5.
// 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    double answer = 0;
    
    int sum = 0;
    
    for (int i = 0; i < numbers.size(); i++)
    {
        sum += numbers[i];
    }
    
    answer = (double)sum / numbers.size();
    
    return answer;
}