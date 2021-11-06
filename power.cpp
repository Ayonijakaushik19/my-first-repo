#include<iostream>
using namespace std;

int main() {
    int x,n;
    cin>>x>>n;
    int pow;
    int i=0;
    while(i<=n){
        if(n>1){
            pow=x*x;
            
        }else if(n==1){
            pow=x*1;
        }else if(n==0||x==1){
            pow=1;
        }
        i+=1;
    }

	cout<<pow;
}
//here we take 0^0=1
