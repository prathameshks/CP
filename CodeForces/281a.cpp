#include <iostream>
using namespace std;

int main() {
    string str;
    cin >> str;
    if (str[0]>95)
    {
        cout<<char(str[0]-32);
    }else
    {
        cout<<str[0];
    }
    
    cout<< str.substr(1,str.size()) <<endl;

    return 0;
}