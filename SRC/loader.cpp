#include "loader.hpp"

void Loader::newGame( Game g )
{
	for( int k = 0; ifstream( ( fileName = "game_" + to_string( k ) + ".txt" ) ).bad(); k++ ); // loop looking for unused file name "game_" + k + ".txt"
	// init file
	writeData( ofstream( fileName ), g );
}

void Loader::loadGame()
{

}


void Loader::autoSave()
{

}

void Loader::saveGame()
{

}

void writeData( ostream& output, Game g )
{
	// player
	output << getTag( "PLAYER", g.m_player );
	// characters
	// TODO create operator<< function for character struct/class?
}

/*
SAVE FILE FORMAT:
player
TODO..
*/