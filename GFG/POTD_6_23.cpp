//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// class Solution {
//   public:
//     int leastInterval(int N, int K, vector<char> &tasks) {
//         // code here
//         int cnt[26] = {0};
//         for(char c:tasks){
//             cnt[c-'A']++;
//         }
//         int ans=0;
//         int k = K;
//         int tempa = 0;
//         int n=N;
//         while(n>0){
//         // for(int i = 0;i<N;i++){
//             if(k<0){
//                 k=K;
//                 tempa = 0;
//             }else{
//                 if(tempa>=26){
//                     ans+=k;
//                     k=K;
//                     tempa=0;
//                 }else if(cnt[tempa]>0){
//                     cnt[tempa]--;
//                     ans++;
//                     n--;
//                     k--;
//                 }
//                 tempa++;
//             }
//         }
//         return ans;
//     }
// };

// class Solution {
//    public:
//     void disp(int a[]) {
//         for (int i = 0; i < 26; i++) {
//             cout << a[i] << " ";
//         }
//         cout << endl;
//     }
//     int leastInterval(int N, int K, vector<char> &tasks) {
//         // code here
//         int cnt[26] = {0};
//         for (char c : tasks) {
//             cnt[c - 'A']++;
//         }
//         int ans = 0;
//         disp(cnt);
//         sort(cnt, cnt + 26);
//         disp(cnt);
//         ans += cnt[25 - K];
//         ans += cnt[25];
//         cout << ans << endl;
//         int f = 0;
//         for (int i = 0; i < K; i++) {
//             if (cnt[25 - i] > cnt[25 - i - 1]) {
//                 f = K - i;
//                 break;
//             }
//         }
//         return (ans * (K + 1)) - f;
//     }
// };

class Solution {
   public:
    void disp(int a[]) {
        for (int i = 0; i < 26; i++) {
            cout << a[i] << " ";
        }
        cout << endl;
    }
    int leastInterval(int N, int K, vector<char> &tasks) {
        // code here
        map<char, int> cnt;  //[26] = {0};
        for (char c : tasks) {
            cnt[c]++;
        }
        int maxf = 0;
        char maxc;
        for (auto i : cnt) {
            if (i.second > maxf) {
                maxf = i.second;
                maxc = i.first;
            }
        }

        int cnt_maxf = 0;

        for (auto i : cnt) {
            if (i.second == maxf) {
                cnt_maxf++;
            }
        }

        int res = max(N, (maxf - 1) * (K + 1) + cnt_maxf);
        return res;
    }
};
int main() {
    int N, K;
    N = 12;
    K = 2;
    vector<char> tasks = {'A', 'A', 'A', 'A', 'A', 'A',
                          'B', 'C', 'D', 'E', 'F', 'G'};
    Solution obj;
    cout << obj.leastInterval(N, K, tasks) << endl;
    return 0;
}

int main2() {
    int t;
    cin >> t;
    while (t--) {
        int N, K;
        cin >> N >> K;

        vector<char> tasks(N);
        for (int i = 0; i < N; i++) cin >> tasks[i];

        Solution obj;
        cout << obj.leastInterval(N, K, tasks) << endl;
    }
    return 0;
}
// } Driver Code Ends