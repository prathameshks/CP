#include <iostream>
#include <cstring>
using namespace std;

class sample {
   public:
    int a;
    char b[10];

    void print() { cout << "a = " << a << " b = " << b << endl; }

    void set(char n[]){
        strcpy(b,n);
    }
};

int main() {
    sample s1;
char c[] = "Sample";

    s1.a = 1;
    s1.set(c);
    sample s2(s1);

    s1.print();
    s2.print();

    s1.b[0] = 'C';

    s1.print();
    s2.print();
    return 0;
}