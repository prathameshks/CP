#include <iostream>
using namespace std;

int main() {
    int t;
    int n, k, ans,tk,fact;
    cin >> t;
    while (t--) {
        cin >> n>>k;
        tk=k;
        fact = 1;
        if(n>k)
            fact =( n/k);
        
        while (n > k) {
            // cout << "x";
            k+=(tk*fact);
            fact = 1;
        }
        ans = k / n;
        if (k % n != 0) {
            ans++;
        }

        cout << ans << endl;
    }
    return 0;
}