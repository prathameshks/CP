//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
   public:
    vector<int> solveQueries(int N, int num, vector<int> &A,
                             vector<vector<int>> &Q) {
        // code here
        map<int, int> count;
        int l, r, k, c;
        vector<int> ans;
        for (int i = 0; i < N; i++) count[A[i]]++;

        for(auto pa:count){
            cout<<"* "<<pa.first<<" - "<<pa.second<<endl;
        }

        for (int p = 0; p < num; p++) {
            c = 0;
            l = Q[p][0];
            r = Q[p][1];
            k = Q[p][2];
            for (int i = l; i <= r; i++) {
                if (count[A[i]] == k) {
                    c++;
                }
            }
            ans.push_back(c);
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        int num;
        cin >> num;
        vector<int> A(N);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
        }
        vector<vector<int>> Q(num, vector<int>(3));
        for (int i = 0; i < num; i++) {
            for (int j = 0; j < 3; j++) {
                cin >> Q[i][j];
            }
        }
        Solution obj;
        vector<int> res = obj.solveQueries(N, num, A, Q);

        for (auto ele : res) {
            cout << ele << " ";
        }
        cout << endl;
    }
}

// } Driver Code Ends