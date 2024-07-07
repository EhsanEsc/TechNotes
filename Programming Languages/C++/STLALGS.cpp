#include <bits/stdc++.h>
// REFRENCES
// https://en.cppreference.com/w/cpp/algorithm
// https://www.youtube.com/watch?v=bFSnXNIsK4A

using namespace std;

template<typename T>
void print(string ss, T x)
{
  auto pr = [](const int& n) { std::cout << " " << n; };
  cout << ss << " : ";
  for_each(x.begin(),x.end(), pr);
  cout << endl;
}

int main()
{
    cout << "##" << endl;

    // for_each by using lambda
    std::vector<int> nums{2, 3, 2, 8, 14, 267};
    print("Befor", nums);
    for_each(nums.begin(), nums.end(), [](int &n){ n++; });
    print("After Modifying by for_each", nums);
    // transform : modify all elemnts by given function
    // also can take two ranges


    cout << "##" << endl;

    /// QUERIES!

    // Numeric Algs

    auto isDivThree = [](int x){ return ((x%3)==0); };
    int cnt = count(nums.begin() , nums.end() , 3);
    int cnt2 = count_if(nums.begin() , nums.end() , isDivThree);
    cout << "Count of Three : " << cnt << " | Count of numbers divisble by 3 : " << cnt2 << endl;

    // accumulate
    // reduce
    // transform_reduce

    // Partial Sum
    vector<int> v(10,2);
    auto dd = [](int x,int y){ return 2*x+y; };
    print("Befor Partial Sum", v);
    partial_sum(v.begin(),v.end(),v.begin());
    print("After Default Partial Sum", v);
    partial_sum(v.begin(),v.end(),v.begin(),dd);
    print("After Partial Sum with lambda", v);

    // (transform_)inclusive_scan
    // (transform_)exclusive_scan

    // adjacent_diffrence
    // sample


    // inner_product
    //  init = binary_op1 (init, binary_op2(*first1,*first2));
    int init = 100;
    int series1[] = {10,20,30};
    int series2[] = {1,2,3};
    cout << "using functional operations: ";
    cout << std::inner_product(series1,series1+3,series2,init,
                                  std::minus<int>(),std::divides<int>());

    cout << "##" << endl;

    // All Any None
    auto isEven = [](int x){ return x%2==0; };
    auto isOdd  = [](int x){ return x%2==1; };
    if(all_of(v.begin(),v.end(),isEven))
      cout << "All Of Them Are EVEN! " << endl;
    if(any_of(v.begin(),v.end(),isDivThree))
      cout << "At least one number divisble by 3 ! " << endl;
    if(none_of(v.begin(),v.end(),isOdd))
      cout << "All of them are not odd!" << endl;

    // Querying a property for 2 ranges
    // equal
    // lexicographical_compare -> first one smaller?
    // mismatch -> first pos they differ : return pair<itr1,itr2>



    cout << "##" << endl;

    /// MOVERS

    // fill copy generate
    auto justDoit = [](){
      static int x=1 ;
      x*=2;
      return x;
    };
    vector<int>vec {1 , 2 , 5 , 7 , 8 , 7 , 2132 , 2 , 7 , 45 , 22 , 3 , 5};
    vector<int>vec2(10) ;
    copy_if(vec.begin() , vec.end() , vec2.begin() , isEven);
    print("Copy_if isEven", vec2);
    fill_n(vec2.begin() , 3 , -22) ; // fill(begin,end,value);
    print("After fill_n", vec2);
    generate(vec2.begin() , vec2.end() , justDoit);
    print("After generate", vec2);
    // iota(first, last, val) : put val into first elemnet then increse it and continue

    // copy_backward
    // move
    // swap_ranges

    cout << "##" << endl;

    /// Modifying whole vector

    print("Before remove", vec);
    vec.erase(remove(vec.begin(),vec.end(),7) , vec.end());
    print("After removing all instance of 7", vec);
    vec.erase(remove_if(vec.begin(),vec.end(),isEven),vec.end());
    print("After remove all instance if isEven", vec);

    // Use When we want to unique vector
    sort(vec.begin() , vec.end() );
    vec.erase(unique(vec.begin(),vec.end()) , vec.end()) ;
    print("After Sort/Unique vector", vec);

    cout << "##" << endl;

    vector<int>vv{12 , 23 , 42 ,123 , 2 ,1 , 3};
    auto it = partition(vv.begin() , vv.end() , isEven) ;
    vector<int> vp1(vv.begin(), it);
    vector<int> vp2(it, vv.end());

    print("Original Vector", vv);
    cout << "Splited By IsEven" << endl;
    print("First half", vp1);
    print("Second half", vp2);

    // reverse , shuffle
    // rotate : Move last elemnt to begining

    // lexicographical_compare
    // is_permutation , next_permutation , prev_permutation

    /// Algorithms on Sets
    // set_diffrences , set_intersection , set_symmetric_difference , set_union
    // includes , merge

    cout << "##" << endl;

    /// Finding Elements

    auto holala = [](int x,int y){ return abs(x)<abs(y); };
    vector<int>::iterator it1 = max_element(vv.begin() , vv.end()) ;
    vector<int>::iterator it2 = max_element(vv.begin() , vv.end() , holala) ;
    // minmax_element : return pair<itr, itr>
    replace(vec.begin() , vec.end() , 2 , 22);
    replace_if(vec.begin() , vec.end() , isOdd , 123) ;

    // IN NOT_SORTED
    // iterator : find(begin,end,value) => find first occurance of value
    // iterator : find_end(begin1,end1,begin2,end2) => find last occurance of (begin2,end2)
    // iterator : find_if(begin,end, somefunction) (Also find_if_not)
    // iterator : find_first_of(begin1,end1,begin2,end2) => find first occurance of any (begin2,end2)
    // adjacent_find

    // IN SORTED
    // binary_search
    // lower_bound , upper_bound
    // equal_range

    // search : find sub_range in anothre range

    cout << "##" << endl;

    /// HEAP

    vv = vector<int>{12 , 23 , 22, -1, 0, 42 ,123 , 2 ,1 , 3};
    print("Before make_heap", vv);

    make_heap(vv.begin(), vv.end());
    print("After make_heap", vv);

    vv.push_back(43);
    push_heap(vv.begin(), vv.end());
    print("After push_heap", vv);

    pop_heap(vv.begin(), vv.end());
    vv.pop_back();
    print("After pop_heap", vv);

    sort_heap(vv.begin(), vv.end());
    print("After sort_heap", vv);

    cout << "##" << endl;

    /// SORTING!

    vv = vector<int>{12 , 23 , 22, -1, 0, 42 ,123 , 2 ,1 , 3};
    // sort(vv.begin(), vv.end());
    print("Befor partial_sort", vv);
    partial_sort(vv.begin(), vv.begin()+5, vv.end());
    print("After partial_sort", vv);

    nth_element(vv.begin(), vv.begin()+vv.size()/2, vv.end());
    print("After nth_elemnt by half", vv);

    // stable_sort , stable_partition , is_partitioned , is_sorted , inplace_merge(Merge two sorted container)

    cout << "##" << endl;

    /// Secret Runes
    // Combine with other algorithms to create new algs!

    // *_copy
    // stable_* : stable_sort, stable_partition
    // *_n : it takes begin and size
    // is_*_until : is_sorted_until -> returns first iterator which is_sorted true until that itr
    // is_* : is_sorted, is_heap
    // *_if

    // Raw Memory

    // uninitialized_* : calls when object is not construct yet
    // uninitialized_fill -> ctor
    // uninitialized_default_construct
    // destroy

}
