#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

int writeFile() {
	std::ofstream wfile{"Sample.txt"};

	if (!wfile) {
		std::cerr << "Womp-womp, can't open the file";
		return 1;
	}

	wfile << "Something\n";
	wfile << "In the way\n";
}

int readFile() {
	std::ifstream rfile{"Sample.txt"};

	if (!rfile) {
		std::cerr << "We can't read file right now";
		return 1;
	}

	// std::string strInput{};
	// while (rfile >> strInput) 
	// 	std::cout << strInput << '\n';

	// Alternative way
	std::stringstream ss_out;
	while (rfile >> ss_out) 
		std::cout << ss_out << '\n';
}

int main() {

	//writeFile();
	readFile();

	return 0;

}