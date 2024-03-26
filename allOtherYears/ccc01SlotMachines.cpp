#include <iostream>

int main(){
    int q, first, second, third;
    int count = 0;
    int current = 1;
    std::cin>>q>>first>>second>>third;
    while (q!=0){
        q-=1;
        if (current == 1){
            first += 1;
            current = 2;
        }
        else if (current == 2){
            second += 1;
            current = 3;
        }
        else{
            third += 1;
            current = 1;
        }
        if (first == 35){
            q+=30;
            first = 0;
        }
        if (second==100){
            q+=60;
            second = 0;
        }
        if (third == 10){
            q+=9;
            third = 0;
        }
        count += 1;
    }
    std::cout<<"Martha plays " << count << " times before going broke.";
}