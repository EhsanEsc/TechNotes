#include<bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(false),cin.tie(0),cout.tie(0)
#define rep(i,vv) for(int i=0;i<(vv);i++)
#define fe(i,vv) for(auto& i:(vv))
#define ll long long
#define pp push_back

const int N = 1e5+22;

int n;

void f(int x)
{
 x++;
}

int main()
{ IOS;
  unique_ptr<int> x(new int(22));
  cout << *x << endl;
  cout << x.get() << endl; // return address
  int* p= x.release(); // Release responsibility for freeing the pointed-to object.
  cout << x.get() << endl;
  x.reset(new int(12));
  cout << x.get() << endl;
  x.reset();
  cout << x.get() << endl;

  // two ways of transfering ownership
  x.reset(new int(22));
  unique_ptr<int> y(x.release());  // use release
  unique_ptr<int> z;
  z = move(y); // use move
  cout << "y: " << y.get() << endl;
  cout << "z: " << z.get() << endl;

  vector<unique_ptr<int>> vec;
  vec.pp(unique_ptr<int>(new int(22)));
  vec.pp(unique_ptr<int>(new int(322)));
  vec.pp(unique_ptr<int>(new int(11)));
  sort(vec.begin(),vec.end());
  fe(u,vec)
    cout << *u << endl;

  unique_ptr<int[]> aa(new int[5]);
  a[0] = 1;   a[2] = 2;

  return 0;
}
