#include <iostream>
using namespace std;

int main() {
    string s1, s2, s3;
    cin >> s1 >> s2 >> s3;
    string s12 = s1 + s2;
    if (s12.size()!=s3.size())
    {
        cout<<"NO"<<endl;
        goto exit;
    }
    
    for (int i = s12.size() - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            if (s12[j] > s12[j + 1]) {
                swap(s12[j], s12[j + 1]);
            }
        }
    }
    for (int i = s3.size() - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            if (s3[j] > s3[j + 1]) {
                swap(s3[j], s3[j + 1]);
            }
        }
    }
    if (s12==s3)
    {
        cout<<"YES"<<endl;
    }else
    {
        cout<<"NO"<<endl;
    }
    
    exit:
    return 0;
}