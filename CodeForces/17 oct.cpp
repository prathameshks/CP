#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int a,b,c;
    int fora,forb;
    for (int i = 0; i < t; i++)
    {
        cin >> a>>b>>c;
        fora = abs(a-1);
        forb = abs(b-c)+abs(c-1);
        if (fora<forb)
        {
            cout<<1<<endl;
        }else if (fora>forb)
        {
            cout<<2<<endl;
        }else{
            cout<<3<<endl;
        }
    }

    return 0;
}