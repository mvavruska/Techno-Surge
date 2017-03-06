// load/update save files for game
#include <iostream>
#include <fstream>
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
	// STRUCT
	static string getTag( string tag, string content ) { return "<" + tag + ">" + content + "<\\" + tag + ">"; }
	// FUNCTIONS
	void newGame( Game );
	void loadGame();
	void readData( istream&, Game );
	void writeData( ostream&, Game );

public:
	Loader( Game*, int ) : fileName( "" ) { }
	void autoSave();
	void saveGame();

};

inline int operator<<( ostream& out, Character c ) { c.print( out ); }