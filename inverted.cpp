#include<iostream>
using namespace std;


int main(){
    int N;
    cin>>N;
    int i=1;
    while(i<=N){
        int j=1;
        while(j<=N-i+1){
            cout<<(N-i)+1;
            j+=1;
        }
        cout<<endl;
        i+=1;
    }

 
}


