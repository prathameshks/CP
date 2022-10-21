#include <iostream>
using namespace std;

int main()
{

    int t, a, b, a1, b1, a2, b2;
    cin >> t;
    while (t--)
    {
        cin >> a >> b >> a1 >> b1 >> a2 >> b2;
        if ((a1 == a and b1 == b) || (a1 == b and b1 == a))
            cout << 1 << endl;
        else if ((a2 == a and b2 == b) || (a2 == b and b2 == a))
            cout << 2 << endl;
        else
            cout << 0 << endl;
    }
    return 0;
}
