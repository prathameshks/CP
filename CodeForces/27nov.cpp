#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;


int main(){
    int n,t,a;
    cin>>n>>t;
    vector<int> b;
    for (int i = 0; i < n; i++)
    {
        cin>>a;
        b.push_back(a);
    }
    sort(b.begin(),b.end());
    int sum=0,i=0;
    while (sum+b[i]<=t && i<n)
    {
        sum+=b[i];
        i++;
    }
    cout<<i<<endl;
    
    return 0;
}