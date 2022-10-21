#include <iostream>
using namespace std;

int main()
{
    int t, amt;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> amt;
        if (amt > 100)
        {
            cout << amt - 10 << endl;
        }
        else
        {
            cout << amt << endl;
        }
    }

    return 0;
}