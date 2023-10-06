#include <iostream>

int get_power(int n, int p) {
	int result = 1;
	for (int i = 0; i < p; i++) {
		result *= 2;
	}
	return result;
}

int main(int argc, char** argv) {
	int result = 0;
	int power = 0;

	for (int i = argc - 1; i > 0; i--) {
		if (std::stoi(argv[i]) == 1) {
			result += get_power(2, power);
		}
		power += 1;
	}
	std::cout << result;
	
	return 0;
}

