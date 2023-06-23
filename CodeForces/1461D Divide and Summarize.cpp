#include <bits/stdc++.h>

#include <iostream>
#include <set>
#include <vector>
using namespace std;

vector<long long int> a;
vector<long long int> presum;
set<long long int> sums;

void solve(int s, int e) {
    sums.insert(presum[e + 1] - presum[s]);

    if (a[s] == a[e]) {
        return;
    }

    int l = s, h = e + 1;
    long long val = (a[s] + a[e]) / 2;
    while (l < h) {
        int mid = l + (h - l) / 2;
        if (a[mid] <= val) {
            l = mid + 1;
        } else {
            h = mid;
        }
    }


    solve(s, h-1);
    solve(h, e);
}

int main() {
    int t, n, q, s;
    cin >> t;
    while (t--) {
        cin >> n >> q;
        a.resize(n, 0);
        presum.resize(n + 1, 0);
        sums.clear();

        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        sort(a.begin(), a.end());

        for (int i = 1; i <= n; i++) {
            presum[i] = a[i - 1] + presum[i - 1];
        }

        solve(0, n - 1);

        while (q--) {
            cin >> s;
            if (sums.find(s) != sums.end()) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        }
    }
    return 0;
}