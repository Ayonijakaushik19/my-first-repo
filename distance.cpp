//Distance between two points
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int x1,y1,x2,y2;
    float dist;
    cin>>x1>>y1>>x2>>y2;
    dist=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
    cout<<dist;
    return 0;
}
