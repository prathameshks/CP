#include <iostream>
using namespace std;


int divide(int a,int b ){
    try
    {
        if (b==0)
        {
            throw(0);
        }
        
        int ans = a/b;
        return ans;
    }
    catch(int a)
    {
        std::cerr << "DIV by Zero\n";
        return a;
    }
    
}


int main(){
    cout<<divide(2,3);
    cout<<divide(2,0);
    return 0;
}