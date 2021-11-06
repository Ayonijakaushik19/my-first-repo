#include<iostream>
using namespace std;


int main(){
     int N;
     cin>>N;
     int i=1;
     int val=1;
     while(i<=N){
         int k=1;//k for taking account of spaces
         while(k<=N-i){
             cout<<" ";
             k+=1;
             
         }
         val=i;
         int j=1;
         while(j<=i){
             cout<<val;
                 j+=1;
                 val+=1;
             
         }
         cout<<endl;
         i+=1;
     }
     
}

