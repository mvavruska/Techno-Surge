#include "loader.hpp"

namespace load
{
	void newGame( Game g )
	{

	}

	void loadGame( Game g )
	{
		// STATIC DATA

		// DYNAMIC DATA

	}


	void autoSave()
	{

	}

	void saveGame()
	{

	}

	void writeData( std::ostream& output, Game g )
	{
		// player
		output << "<PLAYER>" << g.m_player;
		output << "</PLAYER>";
		// characters
		// TODO create operator<< function for character struct/class?
	}

}
/*
SAVE FILE FORMAT:
player
TODO..
*/