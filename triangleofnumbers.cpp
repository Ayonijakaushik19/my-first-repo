#include <iostream>
using namespace std;

int main() {
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
        int val=1;
        val=i;
        while(j<=i){
            cout<<val;
           
            val+=1;
            j+=1;
            
        }
        int k=i-1;
        int start=2*i-2;
        while(k>0){
            cout<<start;
            k=k-1;
            start--;
        }
        cout<<endl;
        i+=1;
    }
    
    
}
