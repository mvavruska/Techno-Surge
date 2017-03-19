#include "game.hpp"

// default values incase create/load fail
Game::Game()
{
	//m_player = Character( new Location( 0, 0, 0 ));	TODO  LOCATION OPTIONS: Location[][][] Location( int, int, int ) Location[]( Tuple )
}

// init some stuff before starting/resume game
void Game::resume()
{
	gameLoop();
}

//
void Game::gameLoop()
{
	while( m_running )
	{
		switch( m_playerState )
		{
			case ALIVE:

				break;
			case DEAD:

		}
	}
}

// action
void Game::action( ACTION a )
{
	switch( a )
	{
		case MOVE:

			break;
		case ATTACK:

			break;
		case FLEE:
		
	}
}

static int menu()
{
	std::cout << "Techno Surge v0.1\n"	<<
				 "------------------\n"	<<
				 "0: Create New Game\n"	<<
				 "1: Load Game\n"		<<
				 "2: Exit\n";
	int x;
	std::cin >> x;
	x = std::max( 0, std::min( 2, x ) );
	return x;
}