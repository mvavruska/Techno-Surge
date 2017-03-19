#pragma once
// load/update save files for game
#include <iostream>
#include <fstream>
#include <string>
#include "game.hpp"
#include "character.hpp"

namespace load
{
	// STRUCT
	static std::string getTag( std::string tag, std::string content ) { return "<" + tag + ">" + content + "<\\" + tag + ">"; }
	// FUNCTIONS
	void newGame( Game );
	void loadGame( Game );
	void readData( std::istream&, Game );
	void writeData( std::ostream&, Game );
};

inline int operator<<( std::ostream& out, Character c ) { c.print( out ); }