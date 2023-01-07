#include <iostream>
using namespace std;




int main(){
    int t;
    cin >> t;
    int a,b,c;
    int aa,ab,ac;
    aa=ab=ac=0;
    while (t--){
        cin>>a>>b>>c;
        aa+=a;
        ab+=b;
        ac+=c;
        // cout<<aa<<ab<<ac<<endl;
    }
        // cout<<aa<<ab<<ac<<endl;
    if ((aa==0) && (ab==0) && (ac==0))
    {
        cout<<"YES"<<endl;
    }else
        cout<<"NO"<<endl;
    
    return 0;
}