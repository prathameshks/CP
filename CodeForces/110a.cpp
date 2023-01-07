#include <iostream>
using namespace std;

bool isLucky(int n) {
    if (n==0)
    {
        return false;
    }
    
    while (n > 0) {
        if (n % 10 != 4 && n % 10 != 7) {
            return false;
        }
        n /= 10;
    }
    return true;
}

int main() {
    long long int num;
    cin >> num;
    long long n = num;
    int cnt = 0;
    while (n > 0) {
        if (n % 10 == 4 || n % 10 == 7) {
            cnt++;
        }
        n /= 10;
    }

    if (isLucky(cnt)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}