#include <iostream>

class Singleton {
private:
    static Singleton* instance; // Static pointer instance of the singleton
    Singleton() { std::cout << "Singleton created!\n"; }    // Basic constructor

public:
    static Singleton* getInstance() {       // Class method for singleton initialization
        if (instance == nullptr) {
            instance = new Singleton();
        }
        return instance;
    }

    void doDomething() {                    // Member function example
        std::cout << "Something is done!\n";
    }
};

Singleton* Singleton::instance = nullptr;       // New instance

int main() {

    Singleton* s1 = Singleton::getInstance();
    Singleton* s2 = Singleton::getInstance();
    s1->doDomething();
    std::cout << "Same instance? " << (s1 == s2 ? "Yes" : "No") << "\n";

    return 0;
}