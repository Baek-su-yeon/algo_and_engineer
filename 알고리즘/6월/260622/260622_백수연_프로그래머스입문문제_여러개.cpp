// 문제 1.
// 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    
    // 방법 1.
    for (int i = 0; i < numbers.size(); i++)
    {
        int num = numbers[i] * 2;
        answer.push_back(num);
    }
    
    // 방법 2.
    // auto: 변수의 자료형을 컴파일러가 자동으로 추론하게 하는 키워드
    // for (변수:배열): python for 변수 in 배열과 동일하게 동작
    for (auto num : numbers) answer.push_back(num * 2);

    return answer;
}

// 문제 2.
// 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = num1 % num2;
    return answer;
}

// 문제 3.
// 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    
    sort(array.begin(), array.end());
    
    // 정렬 (버블 정렬)
    // 정렬 생각나는게 이것 밖에 없네 그냥 한번 읽어보기만 해야할 듯
    for (int i = 0; i < array.size() - 1; i++)
    {
        for (int j = 0; j < array.size() - 1 - i; j++)
        {
            if (array[j] > array[j + 1])
            {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
    
    answer = array[array.size() / 2];
    
    return answer;
}