#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;


int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	priority_queue<int> positive_queue;
	priority_queue<int> negative_queue;

	int n;
	cin >> n;
	for (int i = 0; i < n; i++){
		int command;
		cin >> command;

		if (command > 0) positive_queue.push(-command);
		else if (command < 0) negative_queue.push(command);
		else{
			if (positive_queue.empty() && negative_queue.empty()) cout << 0<<"\n";
			else if (positive_queue.empty()) {
				cout << negative_queue.top()<<"\n";
				negative_queue.pop();
			}
			else if (negative_queue.empty()) {
				cout << -positive_queue.top() << "\n";
				positive_queue.pop();
			}
			else {
				int positive = positive_queue.top();
				int negative = negative_queue.top();
				if (positive > negative) {
					cout << -positive << "\n";
					positive_queue.pop();
				}
				else {
					cout << negative << "\n";
					negative_queue.pop();
				}
			}
		}
	}
}