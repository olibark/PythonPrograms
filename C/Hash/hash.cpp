#include <iostream>
#include <string>
#include <iomanip>
#include <openssl/sha.h>

int main() {
    std::string input;
    std::cout << "Enter input: ";
    std::cin >> input;

    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256(reinterpret_cast<const unsigned char*>(input.c_str()), input.size(), hash);

    std::cout << "SHA-256 hash: ";
    for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i)
        std::cout << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
    std::cout << std::endl;

    return 0;
}