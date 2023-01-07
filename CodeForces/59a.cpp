#include <iostream>
using namespace std;

int main() {
    string str;
    cin >> str;
    int up = 0, down = 0;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] < 96) {
            up++;
            // cout << "UP " << str[i] << endl;
        } else {
            down++;
            // cout << "D " << str[i] << endl;
        }
    }
    if (up > down) {
        for (int i = 0; i < str.size(); i++) {
            if (str[i] > 96) {
                cout << (char)(str[i] - 32);
            } else {
                cout << str[i];
            }
        }
    } else {
        for (int i = 0; i < str.size(); i++) {
            if (str[i] < 96) {
                cout << (char)(str[i] + 32);
            } else {
                cout << str[i];
            }
        }
    }

    return 0;
}