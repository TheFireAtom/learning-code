#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

int writeFile() {
	std::ofstream wfile{"Sample.txt", std::ios::app};

	// we can use wfile.open() for opening the file and wfile.close() to close the same file

	if (!wfile) {
		std::cerr << "Womp-womp, can't open the file";
		return 1;
	}

	wfile << "Something\n";
	wfile << "In the way\n";
	wfile.close();
}

int writeAnotherLinesToFile() {
	std::ofstream outf{"Sample.txt", std::ios::app};

	if (!outf) {
		std::cerr << "We can't open this file, unlucky";
		return 1;	
	}

	outf << "Hmmm...\n";
	outf << "Hmmm...\n";
	outf << std::endl;
	outf.close();

	// Appending line to the file
	outf.open("Sample.txt", std::ios::app);
	outf << "I'm vengeance\n";
	outf.close();
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
	std::string strInput{};
	while (std::getline(rfile, strInput)) 
		std::cout << strInput << '\n';
	rfile.close();
}

int main() {

	writeFile();
	writeAnotherLinesToFile();
	readFile();

	return 0;

}