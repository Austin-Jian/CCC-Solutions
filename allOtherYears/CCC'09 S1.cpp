#include <iostream>
#include <vector>
#include <cmath>

int main(){
    int a, b;
    std::cin >> a >> b;
    int count = 0;
    int cool = 0;
    while (pow(count, 3) <= b) {
        int sr = sqrt(pow(count, 3));
        if (sr * sr == pow(count, 3) and sr*sr >= a) {
            cool += 1;
        }
        count += 1;
    }
    std::cout << cool;
}