#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

int main() {
    std::string og, new_str;
    std::cin >> og >> new_str;

    char funny = '\0';
    char silent = '-';

    std::unordered_set<char> og_set(og.begin(), og.end());
    std::unordered_set<char> new_set(new_str.begin(), new_str.end());

    std::unordered_set<char> checked;
    for (char c : new_str) {
        if (checked.find(c) == checked.end()) {
            checked.insert(c);
            if (og_set.find(c) == og_set.end()) {
                funny = c;
                break;
            }
        }
    }

    std::vector<char> bad;
    for (char c : og_set) {
        if (new_set.find(c) == new_set.end()) {
            bad.push_back(c);
        }
    }

    std::string test1, test2;
    for (char c : og) {
        if (new_set.find(c) != new_set.end()) {
            test1 += c;
            test2 += c;
        } else {
            if (c == bad[0]) {
                test1 += funny;
            }
            if (c == bad.back()) {
                test2 += funny;
            }
        }
    }

    if (test1 == new_str) {
        if (bad[0] != bad.back()) {
            silent = bad.back();
        }
        std::cout << bad[0] << " " << funny << std::endl;
        std::cout << silent << std::endl;
    } else if (test2 == new_str) {
        if (bad[0] != bad.back()) {
            silent = bad[0];
        }
        std::cout << bad.back() << " " << funny << std::endl;
        std::cout << silent << std::endl;
    }

    return 0;
}
