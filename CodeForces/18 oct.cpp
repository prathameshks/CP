#include <iostream>
using namespace std;





int main(){
    int t;
    cin>>t;
    int n,min=0,pos=0;
    char c;
    string a;
    for (int i = 0; i < t; i++)
    {
        cin>>n>>c;
        cin>>a;
        a+=a;
        for(int j =0;j<n;j++){
            if(a[j]==c){
                pos = 0;
                for(int k=j;k<j+n;k++){
                    if(a[k]=='g' and pos>min){
                        min=pos;
                    }
                        pos++;
                }
            }
        }
        cout<<min<<endl;
    }
    
    return 0;
}