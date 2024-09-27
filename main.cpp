#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <cmath>
#include <functional>
#include <bitset>
#include <limits>
#include <iomanip>
#include <tuple>

using namespace std;

// Start of Kashyap Sukshavasi's template for CP
#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define pii pair<int, int>
#define pll pair<long long, long long>
#define all(x) x.begin(), x.end()
#define F first
#define S second

ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return (a / gcd(a, b)) * b; }
bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}
ll modExp(ll base, ll exp, ll mod) {
    ll result = 1;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return result;
}
// End of Kashyap Sukshavasi's template for CP

vector<int> read_ints() {
    string line;
    getline(cin, line);
    istringstream iss(line);
    vector<int> numbers;
    int num;
    while (iss >> num) {
        numbers.push_back(num);
    }
    return numbers;
}

// Function to print a vector of integers
void print_vector(const vector<int>& vec) {
    for (int i = 0; i < vec.size(); ++i) {
        cout << vec[i];
        if (i < vec.size() - 1) {
            cout << " ";
        }
    }
    cout << "\n";
}

int main() {
    fast_io;
    
    int t;
    cin >> t;
    cin.ignore();
    
    while (t--) {
        vector<int> numbers = read_ints();
        print_vector(numbers);
    }
    
    return 0;
}
