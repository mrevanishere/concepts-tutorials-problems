#include <bits/stdc++.h>
#include <iostream>
#define ll long long;
#define arr array;
using namespace std;

class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

// Given a ptr to a node in a connected undirected graph, return copy of graph
// BFS:
Node* sol(Node* node) {
	if (!node) { return nullptr; }
	Node* copy = new Node(node->val, {});
	std::unordered_map<Node*, Node*> copies;
	std::queue<Node*> q;
	q.push(node);
	while (!q.empty()) {
		Node* cur = q.front();
		q.pop();
		for (Node * neighbor : cur->neighbors) {
			if (copies.find(neighbor) == copies.end()) {
				copies[neighbor] = new Node (neighbor -> val, {});
				q.push(neighbor);
			}
			copies[cur]->neighbors.push_back(copies[neighbor]);
		}
	}
	return copy;

}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	// Solution
	// sol();
	return 0;
}
