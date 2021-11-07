#include<iostream>
using namespace std;


int main(){

       int N;
       cin>>N;
       int i;
       while(i<=N){
           int spaces=1;
           while(spaces<=N-i){
               cout<<" ";
               spaces+=1;
               
           }
           int j=1;
           while(j<=i){
               cout<<"*";
               j+=1;
               
           }
           j=i-1;
           while(j>=1){
               cout<<"*";
               j=j-1;
           }
           cout<<endl;
           i+=1;
       }
  
}
