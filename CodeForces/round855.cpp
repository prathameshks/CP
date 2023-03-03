#include <iostream>
using namespace std;

bool check_char(string s) {
    for (int i = 0; i < s.length(); i++) {
        if (!((s[i] == 'M') || (s[i] == 'm') || (s[i] == 'E') ||
              (s[i] == 'e') || (s[i] == 'W') || (s[i] == 'w') ||
              (s[i] == 'O') || (s[i] == 'o'))) {
            return false;
        }
    }
    return true;
}

void lower(string &s) {
    // char c;
    for (int i = 0; i < s.length(); i++) {
        // c = s[i];
        if (s[i] >= 'A' && s[i] <= 'Z') {
            // cout << c;
            s[i] = s[i] - 'A' + 'a';
            // cout<<s[i];
        }
    }
    // cout<<s<<endl;
}

string fold(string s) {
    string ans = "";
    for (int i = 0; i < s.length(); i++) {
        if (ans[ans.length() - 1] != s[i]) {
            ans.push_back(s[i]);
        }
    }
    return ans;
}

bool check(string s) {
    bool res = true;
    char seq[4] = {'m', 'e', 'o', 'w'};
    if (s.length() % 4 != 0) {
        return false;
    }

    for (int i = 0; i < s.length(); i += 4) {
        if (!((s[i] == seq[0]) && (s[i + 1] == seq[1]) &&
              (s[i + 2] == seq[2]) && (s[i + 3] == seq[3]))) {
            return false;
        }
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        string s;
        cin >> n;
        cin >> s;
        if (check_char(s)) {
            lower(s);
            s = fold(s);
            if (check(s)) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }

        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}