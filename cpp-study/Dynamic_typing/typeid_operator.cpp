#include <iostream>
#include <typeinfo>

class Base { virtual void dummy() {} };
class Derived : public Base { /* ... */ };

int main() {
    Base* base_ptr = new Derived;

    // Using typeid to get the type of the object
    std::cout << "Type: " << typeid(*base_ptr).name() << '\n';      // 7Derived as an output, 7 is the length of word "Derived" (g++ compiler thing)

    delete base_ptr;
    return 0;
}