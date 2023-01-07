#include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;

bool ifPossiable(int n, int m, vector<int> arr,long long int mid)
{
    long long chcount = 0;
    int day = 1;
    for (int i = 0; i < m; i++)
    {
        if (chcount + arr[i] <= mid)
        {
            chcount += arr[i];
        }
        else
        {
            day++;
            if (day > n || arr[i] > mid)
            {
                return false;
            }
            chcount = arr[i];
        }
    }
    return true;
}

long long ayushGivesNinjatest(int n, int m, vector<int> time)
{
    long long int s = 0, e = 0, mid, ans;
    for (int i = 0; i < m; i++)
    {
        e += time[i];
    }
    while (s <= e)
    {
        mid = s + (e - s) / 2;
        if (ifPossiable(n, m, time, mid))
        {
            ans = mid;
            e = mid - 1;
        }
        else
        {
            s = mid + 1;
        }
    }
    return ans;
}

int main()
{
    vector<int> a = {1,2,2,3,1};
    cout<<ayushGivesNinjatest(3,5,a);
    return 0;
}