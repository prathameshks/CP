#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    long long int ans = 0;
    int q, n, x, y, k;
    vector<int> steps;
    vector<int> ques;
    for (int i = 0; i < t; i++)
    {
        cin >> n >> q;
        for (int j = 0; j < n; j++)
        {
            cin >> x;
            steps.push_back(x);
        }
        for (int j = 0; j < q; j++)
        {
            cin >> y;
            k = 0;
            ans = 0;
            while (y >= steps[k] and k < n)
            {
                ans += steps[k];
                k++;
            }
            cout << ans << " ";
        }
        cout << endl;
    }

    return 0;
}