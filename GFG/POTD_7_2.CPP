//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution{
    public:
    int cnt=0;
    void disp(int n){
        cout<<cnt++<<" "<<n<<endl;
    }
    int setSetBit(int x, int y, int l, int r){
        // code here
        int lrnum = 0;
        int i = 1;
        int cnt = r-l+1;
        cout<<"L1"<<endl;
        while(cnt--){
            lrnum = lrnum<<1;
            lrnum = lrnum | 1;
            disp(lrnum);
        }
        cout<<"L2"<<endl;
        l--;
        while(l--){
            lrnum = lrnum<<1;
            disp(lrnum);
        }
        cout<<"lrnum"<<endl;
        disp(lrnum);
        int setn = y & lrnum;
        return x|setn;
    }
};

//{ Driver Code Starts.
int main(){
    int t;
    cin>>t;
    while(t--){
        int x, y, l, r;
        cin>>x>>y>>l>>r;
        
        Solution ob;
        cout<<ob.setSetBit(x, y, l, r)<<"\n";
    }
    return 0;
}
// } Driver Code Ends