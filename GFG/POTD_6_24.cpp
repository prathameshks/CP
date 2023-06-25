//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
   public:
    int klengthpref(string arr[], int n, int k, string str) {
        int ans = 0;
        bool isok = true;
        for (int i = 0; i < n; i++) {
            isok = true;
            for (int j = 0; j < k; j++) {
                if (arr[i][j] != str[j]) {
                    isok = false;
                    break;
                }
            }
            if (isok) {
                ans++;
            }
        }

        return ans;
    }
};

int main() {
    string arr[] = {"abba", "abbb", "abbc", "abbd", "abaa", "abca"};
    int n = 6;
    int k = 3;
    string str = "abbbbds";

    Solution ob;
    cout << ob.klengthpref(arr, n, k, str) << endl;

    return 0;
}

//{ Driver Code Starts.
int main2() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string arr[n];
        for (int i = 0; i < n; i++) {
            string s;
            cin >> arr[i];
        }
        int k;
        cin >> k;
        string str;
        cin >> str;

        Solution ob;
        cout << ob.klengthpref(arr, n, k, str) << endl;
    }
    return 0;
}

// } Driver Code Ends