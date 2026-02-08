#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
      string a,b;
      char c;
      int x,y;
      cin>>a>>b;
      x=a.size();
      y=b.size();
      cout<<x<<" "<<y<<endl<<a+b<<endl;
      c=a[0];
      a[0]=b[0];
      b[0]=c;
      cout<<a<<" "<<b;

    return 0;
}

