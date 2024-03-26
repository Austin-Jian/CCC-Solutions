#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    std::vector<std::string> h(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> h[i];
    }

    std::vector<int> ostr;
    for (int i = 0; i < n; ++i) {
        std::vector<int> p;
        int counter = 0;
        while (true) {
            int length = counter + (i + 1);
            if (length > n) {
                break;
            }
            std::vector<std::string> crop(h.begin() + counter, h.begin() + length);
            int asymValue = 0;
            if (crop.size() % 2 == 0) {
                while (!crop.empty()) {
                    asymValue += std::abs(std::stoi(crop.back()) - std::stoi(crop.front()));
                    crop.pop_back();
                    crop.erase(crop.begin());
                }
            } else {
                while (crop.size() > 1) {
                    asymValue += std::abs(std::stoi(crop.back()) - std::stoi(crop.front()));
                    crop.pop_back();
                    crop.erase(crop.begin());
                }
            }
            p.push_back(asymValue);
            counter++;
        }
        ostr.push_back(*std::min_element(p.begin(), p.end()));
    }

    for (const auto& elem : ostr) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    return 0;
}
