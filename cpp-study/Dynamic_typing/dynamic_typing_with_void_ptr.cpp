#include <iostream>

int main() {
    int x = 42;
    float y = 3.14f;
    std::string z = "Hello, world!";

    void* void_ptr;     // void pointer can contain any data dype (as shown below)

    void_ptr = &x;  // int void_ptr
    std::cout << "int value: " << *(static_cast<int*>(void_ptr)) << '\n';   // *() is dereferencing, <int*> because we used void_ptr

    void_ptr = &y;  // float void_ptr
    std::cout << "float value: " << *(static_cast<float*>(void_ptr)) << '\n';

    void_ptr = &z;  // std::string void_ptr
    std::cout << "string value: " << *(static_cast<std::string*>(void_ptr)) << '\n';

    return 0;
#include <iostream>

int main() {
    int x = 42;
    float y = 3.14f;
    std::string z = "Hello, world!";

    void* void_ptr;     // void pointer can contain any data dype (as shown below)

    void_ptr = &x;  // int void_ptr
    std::cout << "int value: " << *(static_cast<int*>(void_ptr)) << '\n';   // *() is dereferencing, <int*> because we used void_ptr

    void_ptr = &y;  // float void_ptr
    std::cout << "float value: " << *(static_cast<float*>(void_ptr)) << '\n';

    void_ptr = &z;  // std::string void_ptr
    std::cout << "string value: " << *(static_cast<std::string*>(void_ptr)) << '\n';

    return 0;
}