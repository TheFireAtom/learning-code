#include <iostream> 

int main() {

	int value = 100;
	int* ptr = &value;
	int result = 0;
	int &ref_result = result;
	result = (*ptr) + 50;
	std::cout << "Result: " << result << std::endl;

	int val = 300;
	int* p = &val;
	int temp = 100;
	int& refTemp = temp;
	std::cout << "refTemp: " << refTemp << std::endl;
	temp = (*p) + 300;
	std::cout << "temp: " << temp << std::endl;
	std::cout << "refTemp: " << refTemp << std::endl;


	return 0;
}