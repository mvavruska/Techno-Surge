// Game Execution; manages all aspects of game
#include "character.hpp"
#include "weapon.hpp"

#include <iostream>
#include <string>
#include <tuple>
#include <algorithm>
#include <vector>
using namespace std;

// ENUM
enum PL_STATE { ALIVE, DEAD };	// player state
// STRUCTS
struct Location
{
	int* m_coords;
	string m_name;

	Location( int x, int y, int z, string n ) : m_coords( new int[]{ x, y, z } ), m_name( n ) { }
};
// lol Matt this ain't Python
struct Action
{
	string keyword;
	string command;

	Action( string k, string c ) : keyword( k ), command( c ) { }
};

class Game
{
public:
	// GLOBALS
	Character m_player;
	// FUNCTIONS
	Game();
	void gameLoop();
private:
	// GLOBALS
	bool m_running;
	PL_STATE m_player_state;	// this might belong better in the character class, will have to be flexible to handle all characters
	// FUNCTIONS

};
