#include <iostream>

void asMemberFunction() {
	class MyClass {
	public: 
		int value;
		MyClass(int v) : value(v) {}
		MyClass operator+(const MyClass& other) const {
			return MyClass(value + other.value);
		}
	};

	MyClass obj1(5);
	MyClass obj2(5);

	MyClass c = obj1 + obj2;

	std::cout << c.value << std::endl;

}

void asNonMemberFunction() {
	class MyAnotherClass {
	public: 
		int value;
		MyAnotherClass(int v) : value(v) {}
		friend MyAnotherClass operator+(const MyAnotherClass& lhs, const MyAnotherClass& rhs) {
			return MyAntoherClass(lhs.value + rhs.value);
		}
	};

	MyAnotherClass object1(5);
	MyAnotherClass object2(5);

	MyAnotherClass object3 = object1 + object2;

	std::cout << object3.value << std::endl;
}

int main() {

	//asMemberFunction();

	asNonMemberFunction();

	return 0;
}

