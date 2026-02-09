#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */      
    int a, b,c;
    cin>>a>>b;
    vector<int> arr[a];

    for(int i=0;i<a;i++)
          {
              int d;
               cin>>c;
            for(int j=0;j<c;j++)
               {
                      cin>>d;
                      arr[i].push_back(d);
               }
          }
  int p,q;
    for(int k=0;k<b;k++)
      {
          cin>>p>>q;
          cout<<arr[p][q]<<endl;
      }
    return 0;
}

