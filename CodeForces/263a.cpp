#include <iostream>
#include <math.h>
using namespace std;

int main() {
    int t;
    int si, sj;
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            cin >> t;
            if (t == 1) {
                si = i;
                sj = j;
            }
        }
    }
    int ans = abs(si-3)+abs(sj-3);
    cout<<ans<<endl;
    return 0;
}