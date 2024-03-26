#include <iostream>

using namespace std;

int main(){
    int d;
    cin>>d;
    while (1){
        int height;
        cin>>height;
        if (height < d){
            d+=height;
        }
        else{
            cout<<d;
            break;
        }
    }
}