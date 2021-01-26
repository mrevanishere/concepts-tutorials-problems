#include <iostream>
using namespace std;

void sol(int n) {
	for (int i = 1; i < n+1; ++i) {
		cout << i << " " << "Abracadabra" << "\n";
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	// Solution
	int n;
	cin >> n;
	sol(n);
	return 0;
}

