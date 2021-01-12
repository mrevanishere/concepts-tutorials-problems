#include <iostream>

template <typename T>
T max(T x, T y) {
	return (x > y) ? x:y;
}

int main() {
	std::cout << max(1, 3) << std::endl;
	std::cout << max('c', 'b') << std::endl;
}
