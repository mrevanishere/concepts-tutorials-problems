#include <iostream>
#include <thread>

void hello() {
    std::cout << "Hello Concurrent\n";
}

int main() {
    std::cout << "Hello World\n";
    std::thread f(hello);
    std::thread h(hello);
    f.join();
    h.join();
}
