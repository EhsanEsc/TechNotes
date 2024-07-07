#include<bits/stdc++.h>

using namespace std;

template<typename...>
using try_to_instantiate = void;

template<typename T,typename = void>
struct is_inc : false_type{};

template <typename T>
struct is_inc<T, try_to_instantiate<decltype(++declval<T &>())>> : true_type{};

template<int N>
struct Fact{
    static int const value = N * Fact<N-1>::value;
};

template<>
struct Fact<0>{
    static int const value = 1;
};

int main()
{
    if(is_inc<string>::value) cout << "!@#" << endl;
    
    if(is_inc<int>::value) cout << "$$$" << endl;

    cout << Fact<10>::value << endl;

    return 0;
}