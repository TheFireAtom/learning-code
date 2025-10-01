#include <iostream>

void swapValues(int* a, int* b) {
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
	std::cout << "Value a: " << a << std::endl;
	std::cout << "Value b: " << b << std::endl;

}

int main() {
	int x = 5;
	int y = 10;
	swapValues(&x, &y);
	std::cout << "Value x: " << x << std::endl;
	std::cout << "Value y: " << y << std::endl;

	return 0;
}