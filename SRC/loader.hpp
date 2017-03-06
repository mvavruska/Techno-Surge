// load/update save files for game
#include <iostream>
#include <string>
using namespace std;
#ifndef GAME
#include "game.hpp"
#endif
#include "character.hpp"

class Loader
{
private:
	// GLOBALS
	std::string fileName;
	// FUNCTIONS

	// STRUCT
	static string getTag( string tag, string content ) { return "<" + tag + ">" + content + "<\\" + tag + ">"; }
public:
	Loader() : fileName( "" ) { }
	void newGame( Game g );
	void loadGame();
	void autoSave();
	void saveGame();

	void readData( istream&, Game );
	void writeData( ostream&, Game );
};

inline operator<<( ostream& out, Tag c		 ) { c.print( out ); }
inline operator<<( ostream& out, Character c ) { c.print( out ); }