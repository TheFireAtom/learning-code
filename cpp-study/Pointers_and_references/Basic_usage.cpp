#include <iostream>

int main() {
    int value = 42;
    
    // 1. Pointer Declaration & Initialization
    int* ptr = &value; // ptr stores the address of 'value'

    // 			   adress | value
  	// (for value)	0x1	  | 42
    // (for ptr)	0x2	  | 42 (same as in the value)

    // 2. Reference Declaration & Initialization
    int& ref = value; // ref is an alias for 'value'

    // So now we have another 

    // Accessing values
    std::cout << "Original Value: " << value << std::endl;
    std::cout << "Value via Reference: " << ref << std::endl; // Access directly
    std::cout << "Value via Pointer (Dereference): " << *ptr << std::endl; // Use *

    // Modifying values (changes the original variable)
    ref = 99; // Changes 'value' to 99
    
    std::cout << "\nValue after reference change: " << value << std::endl;
    
    *ptr = 10; // Changes 'value' to 10
    
    std::cout << "Value after pointer change: " << value << std::endl;

    // Pointer Reassignment (References cannot do this)
    int another_value = 500;
    ptr = &another_value; // ptr now points to 'another_value'
    
    std::cout << "\nPointer now points to a new value: " << *ptr << std::endl;
    // 'ref' is still 10 (it's bound to the original 'value' variable)

    return 0;
}