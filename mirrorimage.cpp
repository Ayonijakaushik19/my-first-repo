#include<iostream>
using namespace std;


int main(){
    int N;
    cin>>N;
    int i=1;
    while(i<=N){
        int spaces=1;
        while(spaces<=N-i){
            cout<<" ";
            spaces+=1;
        }
        int j=1;
        
        while(j<=i){
            
            cout<<j;
            
            j+=1;
        }
        cout<<endl;
        i+=1;
        
    }

  
}
