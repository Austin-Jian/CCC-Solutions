#include <iostream>

int main(){
    double weight;
    std::cin>> weight;
    double height;
    std::cin>> height;
    double bmi = weight/(height*height);
    if (bmi>25){
        std::cout<<"Overweight" <<"\n";
    }
    else if (bmi>=18.5 and bmi<=25){
        std::cout<<"Normal weight" << "\n";
    }
    else{
        std::cout<<"Underweight" <<"\n";
    }
}