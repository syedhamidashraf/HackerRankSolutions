#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    vector <int> arr;
    int n,a;
    cin>>n;

    for(int i=0;i<n;i++)
         {
            cin>>a;
             arr.push_back(a);
         }
      
      for(auto ir=arr.rbegin();ir!=arr.rend();ir++)
            cout<<*ir<<" ";
    return 0;
}
