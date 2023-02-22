#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int arr[100][100];
    int ml[100];
    for (int i = 0; i < n; i++) {
        int temp = INT_MAX;
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
            if (arr[i][j] < temp) {
                temp = arr[i][j];
            }
        }
        ml[i] = temp;
    }

    int maxi = 0;
    for (int i = 0; i < n; i++) {
        if (maxi < ml[i]) {
            maxi = ml[i];
        }
    }
    cout << maxi << endl;

    return 0;
}