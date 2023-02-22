#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    bool condition(int row, int col, int trow, int brow, int lcol, int rcol) {
        bool resr, resc;
        if (row & 1) {
            resr = (trow <= brow);
        } else {
            resr = (trow < brow);
        }
        if (col & 1) {
            resc = (lcol <= rcol);
        } else {
            resc = (lcol < rcol);
        }
        return resr && resc;
    }

    vector<int> spiralOrder(vector<vector<int>>& mat) {
        vector<int> ans;

        int r = mat.size();
        int c = mat[0].size();

        int trow = 0;
        int brow = (mat.size() - 1);
        int lcol = 0;
        int rcol = (mat[0].size() - 1);

        // while (condition(r, c, trow, brow, lcol, rcol)) {
        // while (trow < brow && lcol < rcol) {
        while (trow <= brow && lcol <= rcol) {
            if (trow <= brow) {
                for (int i = lcol; i <= rcol; i++) {
                    ans.push_back(mat[trow][i]);
                }
                trow++;
            }

            if (lcol <= rcol) {
                for (int i = trow; i <= brow; i++) {
                    ans.push_back(mat[i][rcol]);
                }
                rcol--;
            }

            if (trow <= brow) {
                for (int i = rcol; i >= lcol; i--) {
                    ans.push_back(mat[brow][i]);
                }
                brow--;
            }

            if (lcol <= rcol) {
                for (int i = brow; i >= trow; i--) {
                    ans.push_back(mat[i][lcol]);
                }
                lcol++;
            }
        }

        // if (r < c) {
        //     ans.pop_back();
        // }

        return ans;
    }
};

int main() {
    Solution o;
    vector<vector<vector<int>>> ques = {
        {{3}, {4}},
        {{1, 2, 3}},
        {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},
        {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}},
        {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}}};

    vector<int> b;
    for (auto a : ques) {
        b = o.spiralOrder(a);
        for (int x : b) {
            cout << x << " ";
        }
        cout<<endl;
    }

    return 0;
}