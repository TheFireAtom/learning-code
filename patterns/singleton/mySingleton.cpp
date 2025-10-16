#include <iostream>
#include <ctime>
#include <string>

class Logger {
private: 
    static Logger* instance;
    Logger() { std::cout << "Instance is created!\n";}

public: 
    static Logger* getInstance() {
        if (instance == nullptr) {
            instance = new Logger();
        }
        return instance;
    }

    void log(auto message) {
        std::cout << message << "\n";
    }

};

Logger* Logger::instance = nullptr;



int main() {

    Logger* s1 = Logger::getInstance();
    Logger* s2 = Logger::getInstance();
    std::time_t currentTime = std::time(nullptr);
    s1->log(currentTime);
    std::cout << "Same instance?" << (s1 == s2 ? "Yes" : "No") << std::endl;

    return 0;
}

