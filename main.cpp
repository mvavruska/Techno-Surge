// main.cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Location {
	int coords[3];
	string description;
	Location(int[3] coordinates, string desc) {
		coords = coordinates;
		description = desc;
	}
};

class Player {
private:
	bool beatTower;
	bool beatGame;
	bool fled;
	bool died;
};

int main()
{
	vector<Location> visitedlocations;//vector of locations visited
	int code = rand() % 9000 + 1000;
	//start location set to [0,0,0]
	return 0;
}