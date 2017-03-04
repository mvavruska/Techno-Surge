// main.cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Location
{
	int coords[3];
	string description;

	Location( int coordinates[ 3 ], string desc ) :  description( desc )
	{
		for( int k = 0; k < 3; k++ ) coordinates[ k ] = coords[ k ];
	}
};

int main()
{
	//vector of locations visited
	//start location set to [0,0,0]
	return 0;
}