#include<iostream>
using namespace std;


int main(){
       int N;
       cin>>N;
    
       int i=1;
       int val=1;
       while(i<=N){
           val=i;//hm ith row ko i se start kr rhe hai,isliye value jo print krana hai use current row number se reassign kr rhe hai 
           int j=1;
           while(j<=i){
               cout<<val;
               j=j+1;
               val=val+1;
           }
           cout<<endl;
           i+=1;
       }
}
