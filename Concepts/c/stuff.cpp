#include <iostream>

int main() {
    int stuff = 1;
    int *p_stuff = &stuff;
    std::cout << stuff << std::endl;
    std::cout << p_stuff << std::endl;
    std::cout << &stuff << std::endl;
    std::cout << &p_stuff << std::endl;
    std::cout << *p_stuff << std::endl;
    return 0;
}