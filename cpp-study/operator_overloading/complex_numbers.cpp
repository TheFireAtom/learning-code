#include <iostream>

class ComplexNumber {
private: 
		float real;
		float imag;
public:
		ComplexNumber(float r = 0.0f, float i = 0.0f) : real(r), imag(i) {}
		ComplexNumber() {}
		friend ComplexNumber operator+(const ComplexNumber& op1, const ComplexNumber& op2) {
			return ComplexNumber(op1.real + op2.real, op1.imag + op2.imag);
		}

		friend ComplexNumber operator-(const ComplexNumber& op1, const ComplexNumber& op2) {
			return ComplexNumber(op1.real - op2.real, op1.imag - op2.imag);
		}		

		friend ComplexNumber operator*(const ComplexNumber& op1, const ComplexNumber& op2) {
			float real_part = (op1.real * op2.real) - (op1.imag * op2.imag);
			float imag_part = (op1.real * op2.imag) + (op1.imag * op2.real);
			return ComplexNumber(real_part, imag_part);
		}

		friend ComplexNumber operator/(const ComplexNumber& op1, const ComplexNumber& op2) {
			float denominator = op2.real * op2.real + op2.imag * op2.imag;
			if (denominator == 0) {
				throw std::runtime_error("Division by zero");
			}
			float real_part = (op1.real * op2.real + op1.imag * op2.imag) / denominator;
			float imag_part = (op1.imag * op2.real - op1.real * op2.imag) / denominator;
			return ComplexNumber(real_part, imag_part);
		}

	void print() {
		std::cout << real;
		if (imag >= 0) {
			std::cout << "+" << imag << "i";
		} else {
			std::cout << "-" << -imag << "i";
		}
		std::cout << '\n';
	}
};

int main() {

	ComplexNumber num1(3, 4);
	ComplexNumber num2(2, -5);

	ComplexNumber sumResult = num1 + num2;
	ComplexNumber subResult = num1 - num2;
	ComplexNumber multResult = num1 * num2;
	ComplexNumber divResult = num1 / num2;

	sumResult.print();
	subResult.print();	
	multResult.print();
	divResult.print();

	return 0;
}