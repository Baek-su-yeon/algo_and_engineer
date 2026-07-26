#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        int N;
        cin >> N;

        vector<int> position(N + 1);

        for (int locker = 1; locker <= N; ++locker)
        {
            int box;
            cin >> box;

            position[box] = locker;
        }

        vector<bool> visited(N + 1, false);
        vector<int> answer;

        for (int start = 1; start <= N; ++start)
        {
            if (visited[start])
                continue;

            if (position[start] == start)
                continue;

            answer.push_back(start);
            visited[start] = true;

            int current = position[start];

            while (current != start)
            {
                answer.push_back(current);
                visited[current] = true;

                current = position[current];
            }
            answer.push_back(N + 1);
        }

        cout << answer.size() << '\n';

        for (int locker : answer)
            cout << locker << ' ';

        cout << '\n';
    }

    return 0;
}