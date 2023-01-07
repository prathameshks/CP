#include <iostream>
using namespace std;

int main() {
    string str;
    cin >> str;
    string ans;
    int i = 0;
    while (i < str.size()) {
        if (str[i] == '.') {
            ans += '0';
            i++;
        } else {
            if (str[i + 1] == '.') {
                ans += '1';
            } else {
                ans += '2';
            }
            i += 2;
        }
    }
    cout<<ans<<endl;
    return 0;
}