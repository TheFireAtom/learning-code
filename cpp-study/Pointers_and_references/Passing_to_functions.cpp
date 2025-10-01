#include <iostream>

// Pass-by-Value: Makes a copy (inefficient for large objects)
void byValue(int x) {
    x = 1; // Changes only the copy
}

// Pass-by-Reference: Changes the original variable directly (efficient and clear)
void byReference(int& x) {
    x = 2; // Changes the original variable
}

// Pass-by-Pointer: Changes the original variable using dereferencing
void byPointer(int* x) {
    if (x != nullptr) {
        *x = 3; // Changes the original variable
    }
}

int main() {
    int num = 100;
    
    byValue(num);
    std::cout << "After byValue: " << num << std::endl; // Output: 100

    byReference(num);
    std::cout << "After byReference: " << num << std::endl; // Output: 2

    byPointer(&num); // Must pass the ADDRESS
    std::cout << "After byPointer: " << num << std::endl; // Output: 3
    
    return 0;
}