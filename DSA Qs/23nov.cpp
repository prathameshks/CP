#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;




int main(){
    int t;
    int n,ans,elmt;
    cin >> t;
    while (t--){
        cin>>n;
        vector<int> nums[n];
    ans = 0;
    for (int i = 0; i < n; i++)
    {
        cin>>elmt;
        ans^=elmt;
        nums->push_back(elmt);
    }
    vector<int>::iterator iter = nums->begin();
        if(find(nums->begin(),nums->end()+1,ans)){
            cout
        }
    }
    return 0;
}