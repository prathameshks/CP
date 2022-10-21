// day 
#include <iostream>
using namespace std;


class Person{
    public:
        string name;
        int age;
        int number;
        virtual void getdata();
        void putdata(){
            cout<<name<<" "<<age<<" "<<number<<endl;
        }
};
class Professor:public Person{
    public:
    void getdata(){
        cin>>name>>age>>number;
    }
};
class Student:public Person{
    public:
    int n1,n2,n3,n4,n5,n6;
    void getdata(){
        cin>>name;
        cin>>age;
        cin>>n1>>n2>>n3>>n4>>n5>>n6;
        number = n1+n2+n3+n4+n5+n6;
    }
};



int main(){
	
	return 0;
}