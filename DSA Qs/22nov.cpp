#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    int a, b, c, paracheck;
    char max;
    string str, ans;
    bool first;

    while (t--)
    {
        cin >> str;
        a = 0;
        b = 0;
        c = 0;
        ans = "YES";
        first = true;
        paracheck = 0;
        for (int i = 0; i < str.size(); i++)
        {
            switch (str[i])
            {
            case 'A':
                a++;
                break;

            case 'B':
                b++;
                break;

            case 'C':
                c++;
                break;
            }
        }
        if (a > b && a > c)
        {
            // a
            max = 'A';
            if (a != b + c)
            {
                ans = "NO";
                goto end;
            }
        }
        else if (b > a && b > c)
        {
            // b
            max = 'B';
            if (b != a + c)
            {
                ans = "NO";
                goto end;
            }
        }
        else
        {
            // c
            max = 'C';
            if (c != b + a)
            {
                ans = "NO";
                goto end;
            }
        }
        if (str[0] != max)
        {
            first = false;
        }

        for (int j = 0; j < str.size(); j++)
        {
            if (first)
            {

                if (str[j] == max)
                {
                    paracheck++;
                }
                else
                {
                    paracheck--;
                }
            }
            else
            {

                if (str[j] != max)
                {
                    paracheck++;
                }
                else
                {
                    paracheck--;
                }
            }

            if (paracheck < 0)
            {
                ans = "NO";
                goto end;
            }
        }

    end:
        cout << ans << endl;
    }
    return 0;
}