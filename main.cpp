#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <cmath>
#include <functional>
#include <bitset>
#include <limits>
#include <iomanip>
#include <tuple>

std::vector<int> read_ints() {
    std::string line;
    std::getline(std::cin, line);
    std::istringstream iss(line);
    std::vector<int> numbers;
    int num;
    while (iss >> num) {
        numbers.push_back(num);
    }
    return numbers;
}

void print_vector(const std::vector<int>& vec) {
    for (int i = 0; i < vec.size(); ++i) {
        std::cout << vec[i];
        if (i < vec.size() - 1) {
            std::cout << " ";
        }
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> numbers;
    std::string line;
    
    while (std::getline(std::cin, line)) {
        numbers = read_ints();
    }

    return 0;
}
