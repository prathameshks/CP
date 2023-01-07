#include <bits/stdc++.h>
using namespace std;

class Solution {
   public:
    bool comp(map<char, int> m1, map<char, int> m2) {
        for (auto p : m1) {
            if (p.second != m2[p.first]) {
                return false;
            }
        }
        return true;
    }

    bool checkInclusion(string s1, string s2) {
        map<char, int> m1;
        int n1 = s1.size(), n2 = s2.size();
        for (char c : s1) {
            m1[c]++;
        }
        for (int i = 0; i <= (n2 - n1); i++) {
            map<char, int> m2;
            for (int j = i; j < i + n1; j++) {
                m2[s2[j]]++;
            }
            if (comp(m1, m2)) {
                return true;
            }
        }
        return false;
    }
};

int main() {
    Solution obj;
    cout << obj.checkInclusion("adc", "dcda") << endl;
}