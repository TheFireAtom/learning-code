#include <iostream>
#include <any>

int main() {
    std::any any_value;     // usage of std::any

    any_value = 42;     // can be int
    std::cout << "int value: " << std::any_cast<int>(any_value) << '\n';    // same principle that we used with void_ptr, but now we don't use pointers

    any_value = 3.14;   // can be float
    std::cout << "double value: " << std::any_cast<double>(any_value) << '\n';

    any_value = std::string("Hello, world!");   // can be std::string
    std::cout << "string value: " << std::any_cast<std::string>(any_value) << '\n';

    return 0;
}
