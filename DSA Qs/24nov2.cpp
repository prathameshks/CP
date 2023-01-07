#include <iostream>
using namespace std;

int main()
{
    int n, k, ans = 0;
    cin >> n >> k;
    int rem = 240 - k, i = 1;
    while (rem >= 0 && i<=n+1)
    {
        rem -= (i * 5);
        ans++;
        i++;
    }
    cout << ans - 1 << endl;
    return 0;
}