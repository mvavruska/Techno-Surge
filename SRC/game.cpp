#include "game.hpp"
#include <iostream>
using namespace std;

int Game::menu()
{
	cout << "Techno Surge v0.1\n" <<
			"------------------\n" <<
			"0: Create New Game\n" <<
//TODO		"1: Load Game\n" <<
			"2: Exit\n";
	int x;
	cin >> x;
	return 0;
}

// init
Game::Game( int x )
{
	switch( x )
	{
		case 0: // create new game
			Loader::newGame();
			break;
	}
}