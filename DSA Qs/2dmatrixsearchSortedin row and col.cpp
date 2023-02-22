#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size();
        int col = matrix[0].size();

        int r = 0, c = col - 1;
        while (r < row && c >= 0) {
            int mid = matrix[r][c];
            if (mid == target) {
                return 1;
            } else if (mid < target) {
                r++;
            } else {
                c--;
            }
        }
        return 0;
    }
};

int main() {
    vector<vector<int>> a = {{1, 4, 7, 11, 15},
                             {2, 5, 8, 12, 19},
                             {3, 6, 9, 16, 22},
                             {10, 13, 14, 17, 24},
                             {18, 21, 23, 26, 30}};
    Solution obj;
    // cout<<obj.searchMatrix(a,5);
    cout << obj.searchMatrix(a, 56);
    return 0;
}