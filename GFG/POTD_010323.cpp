//{ Driver Code Starts
// Initial Template for C++

#include <iostream>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

void print(vector<int> &a) {
    for (int i : a) {
        cout << i << " ";
    }
    cout << endl;
}

class Solution {
   public:
    vector<int> updateQuery(int N, int Q, vector<vector<int>> &U) {
        // code here
        vector<int> a(N, 0);
        int i, j;
        for (i = 0; i < Q; i++) {
            for (j = (U[i][0] - 1); j < U[i][1]; j++) {
                a[j] |= U[i][2];
            }
        }
        return a;
    }
};

/*
3 2
1 3 1
1 3 2
*/

//{ Driver Code Starts.

int main() {
    int t;
    // cin >> t;
    t = 1;
    while (t--) {
        int n, q;
        cin >> n >> q;
        vector<vector<int>> u(q, vector<int>(3));
        for (int i = 0; i < q; i++) cin >> u[i][0] >> u[i][1] >> u[i][2];
        Solution a;
        vector<int> ans = a.updateQuery(n, q, u);  //<<endl;
        for (auto j : ans) {
            cout << j << " ";
        }
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends