//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
    int mod = pow(10, 9) + 7;

    int binaryexp(int x, int n) {
        if (n == 0) return 1;
        int temp = binaryexp(x, n / 2);
        if (n % 2 == 0)
            return (1LL * temp * temp) % mod;
        else
            return (((1LL * temp * temp) % mod) * x) % mod;
    }

   public:
    int nCr(int n, int r) {
        // code here
        if (r > n) {
            return 0;
        }
        int r1, r2;
        if (r > n / 2) {
            r1 = r;
            r2 = n - r;
        } else {
            r1 = n - r;
            r2 = r;
        }
        // cout<<temp;
        long long num = 1;
        for (int i = n; i > r1; i--) {
            num = (num * i) % mod;
        }

        for (int i = r2; i > 0; i--) {
            int inv = binaryexp(i, mod - 2);
            num = (num * inv) % mod;
        }

        return num;
    }
};

//{ Driver Code Starts.

int main() {
    int n, r;
    Solution ob;
    cout << ob.nCr(69, 43) << endl;

    return 0;
}
int main2() {
    int t;
    cin >> t;
    while (t--) {
        int n, r;
        cin >> n >> r;

        Solution ob;
        cout << ob.nCr(n, r) << endl;
    }
    return 0;
}
// } Driver Code Ends