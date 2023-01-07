#include <bits/stdc++.h>
using namespace std;

class Solution {
   public:
    void reverse(string &s, int i, int j) {
        // cout<<i<<j<<endl;
        j--;
        while (i < j) {
            swap(s[i], s[j]);
            i++;
            j--;
        }
    }

    string reverseWords(string s1) {
        string s = s1;
        int i = 0;
        for (int j = 0; j < s.size(); j++) {
            if (s[j] == ' ') {
                reverse(s, i, j);
                i = j + 1;
            }
        }
        reverse(s, i, s.size());
        return s;
    }
};

int main() {
    string s = "Helo how are yput gbf? 'dfk,, f";
    Solution obj;
    cout << s<<endl;
    cout<<obj.reverseWords(s);

}