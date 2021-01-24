#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define ll long long
#define ar array 

// strong if:
// 6 <= n <= 20
// contains >= 1 lowercase letter
// contains >= 1 uppercase letter
// contains >= 1 digit
// does not contain >= 3 characters in a row

// return minimum steps required to make password strong

// One step is: insert, delete, or replace a char

// Best: O(n)
// int repeating = 0;
// bool lower = false;
// bool upper = false;
// vector<pair> indexes;
// for c in str:
//	if current = previous:
//		++repeating;
//	else if repeating >= 3:
//		indexes.pb(i-repeating,i);
//	if char is lowercase:
//		lower = true;
//	if char is uppercase:
//		upper = true;
// return n.size() reduced to bounds and 
// +1 if lower = false and +1 if upper = false and
// +n
//
//
// Case: aaa aaa aaa aaa
// aab aab aab baa
// so 1 for every n//3
#include <utility>
#include <locale>
#include <string>
int sol(string password) {
	int repeating = 0;
	int lower = 0;
	int upper = 0;
	int digit = 0;
	vector<pair<int, int>> indexes;
	char curr;
	char prev;
	int n = password.size();
	for (int i = 0; i < n; ++i) {
		if (islower(password[i])) {
			lower = 0;
		}
		if (isupper(password[i])) {
			upper = 0;
		}
		if (isdigit(password[i])) {
			digit = 0;
		}
		curr = password[i];
		if (curr == prev) {
			++repeating;
		} 
		else if (repeating >= 3) {
			indexes.emplace_back(pair<int, int>{i-3,i});
		}
		else {
			repeating = 0;
		}
	}
	if (n > 20) {
		return n-20 + max(indexes.size()/3, lower + upper + digit);
	}
	if (n < 6) k {
		return max(indexes.size()/3, lower + upper + digit);
	}
	if (n <= 20) {
		return max(indexes.size()/3, lower + upper + digit);
	}
}

int main() {
	std::ios::sync_with_stdio(0);
	cin.tie(0);
	// solution
	string a = "aaaaa";
	cout << sol(a);
	return 0;
}
