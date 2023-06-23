#include <iostream>
#include <vector>
using namespace std;
vector<int> h;
int m;

int binarySearch(int s, int e) {
    int mid = ((s + e) / 2);
    long long sum = 0;
    for (int i = 0; i < h.size(); i++) {
        if (h[i] > mid) {
            sum += (h[i] - mid);
        }
    }

    if (sum == m) {
        return mid;
    } else if (sum < m) {
        return binarySearch(s, mid - 1);
    } else {
        return binarySearch(mid + 1, e);
    }
}

int main() {
    int n;
    int e = 0;
    cin >> n >> m;

    h.resize(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> h[i];
        if (h[i] > e) e = h[i];
    }
    int ans = binarySearch(0, e);
    cout << ans << endl;

    return 0;
}