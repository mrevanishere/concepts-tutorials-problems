#include <iostream>
#include <thread>

void hello() {
    std::cout << "Hello Concurrent\n";
}

int main() {
    std::cout << "Hello World";
    std::thread f(hello);
    f.join();
}
