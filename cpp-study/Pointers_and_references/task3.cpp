#include <iostream>

void increment_integer(int& p) {
	p++;
	std::cout << "Value p: " << p << std::endl;
}

int main() {

	int x = 10;
	increment_integer(x);
	std::cout << "Value x: " << x << std::endl;


	return 0;
}