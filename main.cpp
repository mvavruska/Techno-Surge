// main.cpp
#include <iostream>
#include <string>
#include <vector>
#include "character.hpp"
#include "weapon.hpp"
using namespace std;

// GLOBALS
Character m_player;
// STRUCTS
struct Location
{
	int coords[ 3 ];
	string description;

	Location( int coordinates[ 3 ], string desc ) :  description( desc )
	{
		for( int k = 0; k < 3; k++ ) coordinates[ k ] = coords[ k ];
	}
};

int main()
{
	// player; start location [0,0,0]
	m_player = Character( new Location( new int[]{ 0, 0, 0 }, "" ));

	return 0;
}