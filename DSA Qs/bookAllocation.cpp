#include <iostream>
#include <vector>
using namespace std;

bool isPossiable(vector<int> arr, int n, int m, int mid)
{
    int temp;
    int cur = 0, stu = 1;
    temp = 0;
    while (cur < n)
    {
        if ((temp + arr[cur]) <= mid)
        {
            temp += arr[cur];
        }
        else
        {
            stu++;
            if (stu > m || arr[cur] > mid)
            {
                return false;
            }
            temp = arr[cur];
        }
        cur++;
    }
    return true;
}

int allocateBooks(vector<int> arr, int n, int m)
{
    // Write your code here.
    int tempAns = -1;
    int s = 0, mid, e = 0;
    for (int i = 0; i < n; i++)
    {
        e += arr[i];
    }

    while (s <= e)
    {
        mid = s + (e - s) / 2;

        if (isPossiable(arr, n, m, mid))
        {
            tempAns = mid;
            e = mid - 1;
        }
        else
        {
            s = mid + 1;
        }
    }
    return tempAns;
}

int main()
{
    vector<int> a = {10, 20, 30, 40};
    int ans = allocateBooks(a, 4, 2);
    cout << ans;
    return 0;
}