#include <iostream>
#include<iomanip>
using namespace std;

int sqrtInt(int x)
{
    long long int square, mid, ans;
    int s, e;
    s = 0;
    e = x;
    while (s <= e)
    {
        mid = s + (e - s) / 2;
        square = mid * mid;
        if (square > x)
        {
            e = mid - 1;
        }
        else if (square < x)
        {
            s = mid + 1;
            ans = mid;
        }
        else
        {
            return mid;
        }
    }
    return ans;
}

double sqrtDecimal(int num,int root,int iters){
    double tempAns = root;
    double incr=1;
    double no=root;
    int i;
    while (iters--)
    {
        incr *=0.1;
        i=0;
        while (no*no < num && i<10)
        {
            tempAns = no;
            no+=incr;
            i++;
        }
        if (no*no == num)
        {
            cout<<"Val\n";
            return no;

        }
        
    }
    return tempAns;
}


int main()
{
    int num = 108;
    int r = sqrtInt(num);
    double root = sqrtDecimal(num,r,5);
    
    cout<<setprecision(10)<<root;
    return 0;
}