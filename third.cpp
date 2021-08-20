//To print multiple words ,we use getline

#include <iostream>
using namespace std;
int main()
{
    string name;
    cout<<"May i know your name"<<" ";
    getline(cin,name);
    cout<<name;
    return 0;
}
