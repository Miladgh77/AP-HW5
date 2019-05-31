#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <numeric>
//#include <execution> couldn't use this lib properly!!

void show(std::vector<int> a);
int main()
{
  std::vector<int> vec1(100);
  std::vector<int> vec2(10);

  std::iota(vec1.begin(), vec1.end(), 1);
  std::cout<<"******************vec1*******************" <<std::endl;
  show(vec1);
  std::iota(vec2.begin(), vec2.end(), 1);
  std::cout<<"******************vec2*******************" <<std::endl;
  show(vec2);
  //////////////////////////////////////////////
  vec2.insert(vec2.end() , vec1.begin() , vec1.end());
  std::cout<<"**************vec1 appended to vec2******************" <<std::endl;
  show(vec2);
  /////////////////////////////////////////////////    
  std::vector<int>odd_vec(vec1.size());
  auto it = std::copy_if(vec1.begin() , vec1.end() , odd_vec.begin() ,[](int i){return i%2==1;});
  odd_vec.resize(std::distance(odd_vec.begin() , it));
    std::cout<<"*******************odd_vec :****************" <<std::endl;
  show(odd_vec);
  ////////////////////////////////////////////////
  std::vector<int>reverse_vec(100);
  std::reverse_copy(std::begin(vec1), std::end(vec1) , std::begin(reverse_vec));
  std::cout<<"*****************reverse_vec******************" <<std::endl;
  show(reverse_vec);
  ////////////////////////////////////////////////  
  std::sort(vec2.begin(), vec2.end(), std::less<int>());
   std::cout<<"****************vec2 sorted******************" <<std::endl;
   show(vec2);
  //std::sort(std::execution::par, vec2.begin(), vec2.end(),[&](int));

  return 0;
}

void show(std::vector<int> a)
{
  for(size_t i =0; i<a.size();i++)
    std::cout<< a[i]<<" ";
  std::cout<<std::endl<<std::endl;
}


