#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int x, y, ans;
        cin >> x >> y;
        if (x & 1) {
            // if(1){
            vector<bool> primes(y + 1, 1);
            primes[0] = 0;
            primes[1] = 0;
            for (int q = 2; q * q <= y; q++) {
                if (primes[q]) {
                    for (int s = q * q; s <= y; s += q) {
                        primes[s] = 0;
                    }
                }
            }
            vector<int> prs;
            for (int j = 2; j <= y; j++) {
                if (primes[j]) {
                    prs.push_back(j);
                }
            }

            ans = 0;
            while (x < y) {
                for (int p = 0; p < prs.size(); p++) {
                    if ((x % prs[p]) == 0) {
                        // cout<<"* "<<x<<" "<<prs[p]<<endl;
                        x += prs[p];
                        break;
                    }
                }

                ans++;
            }
        } else {
            ans = (y + 1 - x) / 2;
        }

        cout << ans << endl;
        // for(int a:prs){
        //     cout<<a<<" ";
        // }
    }
    return 0;
}
