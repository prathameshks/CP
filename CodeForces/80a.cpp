#include <iostream>
#include <vector>
using namespace std;

bool isPrime(int n, vector<int> primes) {
    for (auto j : primes) {
        if (n % j == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int n, y;
    cin >> n >> y;
    vector<int> primes;
    primes.push_back(2);
    bool prime = true;
    for (int i = 3; i <= y; i += 2) {
        if (isPrime(i, primes)) {
            primes.push_back(i);
        }
    }
    if (primes.back() == y && primes[primes.size() - 2] == n) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
        /* code */
    }

    return 0;
}