#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    int n, h;
    int m1, m2, temp, ans;
    bool button;
    while (t--)
    {
        cin >> n >> h;
        m1 = 0;
        m2 = 0;
        button = true;
        ans = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> temp;
            if (temp > m1)
            {
                m2 = m1;
                m1 = temp;
            }else if (temp>m2)
            {
                m2=temp;
            }
            
        }
            // cout<<m1<<" "<<m2<<endl;
        while (h > 0)
        {
            ans++;
            // cout<<"h"<<h<<endl;
            if (button)
            {
                button = false;
                h -= m1;
            }
            else
            {
                button = true;
                h -= m2;
            }
        }
        // cout << "*";
        cout << ans << endl;
    }
    return 0;
}