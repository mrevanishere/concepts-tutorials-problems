#include <iostream>
#include <string>
using namespace std;

string defangIPaddr(string address) {
	return std::replace(address.begin(), address.end(), ".", "[.]");
}

int main() {
	return 0;
}
