//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
   public:
    int distributeTicket(int N, int K) {
        // code here
        if (N <= K) {
            return N;
        }
        int p = 1;
        int pl = N;
        bool turn = true;

        while ((pl - p) > K) {
            if (turn) {
                p += K;
            } else {
                pl -= K;
            }
            turn = !turn;
        }
        // cout << p << " " << pl << endl;

        if (turn) {
            return pl;
        } else {
            return p;
        }
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {
        int N;
        scanf("%d", &N);

        int K;
        scanf("%d", &K);

        Solution obj;
        int res = obj.distributeTicket(N, K);

        cout << res << endl;
    }
}

// } Driver Code Ends