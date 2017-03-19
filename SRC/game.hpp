#pragma once
// Game Execution; manages all aspects of game
#include "character.hpp"
#include "weapon.hpp"

#include <iostream>
#include <string>
#include <tuple>
#include <algorithm>
#include <vector>

// ENUM
enum MENU		{ NEW, LOAD, EXIT };
enum PL_STATE	{ ALIVE, DEAD };	// player state
enum ACTION		{ MOVE, ATTACK, FLEE };
// STRUCTS
struct location
{
	int x, y, z;
	std::string name;
	location( int p_x, int p_y, int p_z, std::string p_name ) : x( p_x ), y( p_y ), z( p_z ), name( p_name ) { }
};

struct action
{
	std::string keyword;
	std::string command;

	action( std::string k, std::string c ) : keyword( k ), command( c ) { }
};

bool operator==( location& a, location& b )
{
	return a.x == b.x && a.y == b.y && a.z == b.z;
}

class Game
{
public:
	// GLOBALS
	Character m_player;
	// FUNCTIONS
	Game();
	void resume();
	static int menu();
private:
	// GLOBALS
	bool m_running, m_victory;
	PL_STATE m_playerState;	// this might belong better in the character class, will have to be flexible to handle all characters
	std::vector<location> m_visited;
	// FUNCTIONS
	void gameLoop();
	void action( ACTION );
};
