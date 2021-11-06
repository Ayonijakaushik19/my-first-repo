#include<iostream>
using namespace std;

int main() {
	int N;
    int odd_sum=0;
    int even_sum=0;
    int i;
    
    int rem;
    cin>>N;
 //N>=0 will give infinite loop,in tht case we can get time limit exceeded error  
	while (N>0){
        rem=N%10;
        
        if(rem%2==0){
            even_sum+=rem;
        }else{
            odd_sum+=rem;
        }
        N=N/10;
    }
    cout<<even_sum<<" "<<odd_sum;
}
