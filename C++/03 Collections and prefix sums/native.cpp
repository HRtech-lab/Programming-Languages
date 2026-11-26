#include <iostream>
#include <iomanip>
#include <numeric>
#include <iterator>
#include <vector>

int main() {
    std::cout << std::setprecision(12);
    const std::vector changes{3, -1, 4, -2, 0, 2};
    std::vector<int> balances;
    std::partial_sum(changes.begin(), changes.end(), std::back_inserter(balances));
    for (int value : balances) std::cout << value << ' ';
}
