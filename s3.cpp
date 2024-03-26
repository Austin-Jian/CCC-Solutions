#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

int main() {
    std::string n, h;
    std::cin >> n >> h;

    std::sort(n.begin(), n.end());
    std::unordered_set<std::string> permDistinct;

    do {
        permDistinct.insert(n);
    } while (std::next_permutation(n.begin(), n.end()));

    int count = 0;
    for (const auto& perm : permDistinct) {
        if (h.find(perm) != std::string::npos) {
            count++;
        }
    }

    std::cout << count << std::endl;

    return 0;
}