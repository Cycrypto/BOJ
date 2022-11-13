#include <iostream>
#include <queue>
using namespace std;

int main(){
    queue<int> qu;
    qu.push(1);
    qu.push(9);
    qu.push(5);

    int sz = qu.size();
    for(int i = 0; i < sz; i++){
        cout << qu.front() << ',';
        qu.pop();
    }cout << '\n';

    priority_queue<int> pqu;
    pqu.push(1);
    pqu.push(9);
    pqu.push(5);

    sz = pqu.size();
    
}