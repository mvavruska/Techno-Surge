// Game Execution; manages all aspects of game
#include "character.hpp"
#include "weapon.hpp"
#include "loader.hpp"

class Game
{
private:
	// GLOBALS
	Loader m_game;
	Character m_player;
	// STRUCTS
	struct Location
	{
		int coords[ 3 ];
		string description;

		Location( int coordinates[ 3 ], string desc ) : description( desc )
		{
			for( int k = 0; k < 3; k++ ) coordinates[ k ] = coords[ k ];
		}
	};
	struct Action
	{
		string keyword;
		string command;

		Action( string k, string c ) : keyword( k ), command( c );
	};
public:

};