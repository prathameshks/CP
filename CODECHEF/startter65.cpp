#include <iostream>
#include<map>
using namespace std;

int main() {
	
	int t,n,elmt;
	cin>>t;
	for (int i =0;i<t;i++){
	    map<int, int> freq;
	    cin>>n;
	    for (int j = 0; j < 2*n; j++) {
	        cin>>elmt;
	        freq[elmt]++;
	    }
	    
	    bool possiable=true;
	    for (auto it : freq) {
	        std::cout <<"*"<< it.first<<it.second << std::endl;
	        if(it.second >2){
	            possiable = false;
	            break;
	        }
	    }
	    if(possiable)
	        cout<<"Yes"<<endl;
	    else
	        cout<<"No"<<endl;
	    
	}
	return 0;
}
