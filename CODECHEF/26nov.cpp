#include <iostream>
#include <set>
using namespace std;

int main()
{
    string s;
    cin >> s;
    set<char> dist;
    for (int i = 0; i < s.size(); i++)
    {

        dist.insert(s[i]);
    }
    int numchar = dist.size();
    if (numchar % 2 == 0)
    {
        cout << "CHAT WITH HER!" << endl;
    }
    else
    {

        cout << "IGNORE HIM!" << endl;
    }

    return 0;
}