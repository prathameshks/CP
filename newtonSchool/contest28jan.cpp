#include <bits/stdc++.h> // header file includes every Standard library
using namespace std;

int main() {
	// Your code here
    int a,b,c,ans;
    cin>>a>>b>>c;
    if((a+b) > 0 && not ((a+b)&1)){
        cout<<"YES"<<endl;
    }else if((c+b) > 0 && not ((c+b)&1)){
        cout<<"YES"<<endl;
    }else if((a+c) > 0 && not ((a+c)&1)){
        cout<<"YES"<<endl;
    }else{
        cout<<"NO"<<endl;
    }
    return 0;
}
