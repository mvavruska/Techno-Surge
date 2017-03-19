// main.cpp
// starting point, setup Game class
#include "game.hpp"
#include "loader.hpp"

int menu();

// program execution start point
int main()
{
	Game game = Game();				// setup
	int option = Game::menu();		// menu new:load:exit
	switch( option )
	{
		case NEW:
			load::newGame( game );
			game.resume();
			break;
		case LOAD:
			load::loadGame( game );
			game.resume();
			break;
		default:
	}
	

	// MOVE TO GAME.CPP....
	// m_player = Character();
	// int[] location, location2 = { 0,0,0 };	// locations will be loaded by file, character set to Location { 0, 0, 0 }
	/*
	std::vector<int[]> visitedlocations;
	vector<Location> locations;
	int passcode = 1234; //will need to be randomly generated between 1000-9999
	bool victory = true;
	bool gameover, gamebeaten, dead, TowerBeaten, fled = false;
	std::cout << "prologue goes here..." << std::endl; // will eventually print prologue
	while (!gameover)
	{
		while (!gamebeaten)
		{
			while (!dead)
			{
				while (!TowerBeaten)
				{
					if (!fled)
					{
						if (location != [1, 1, 1])
						{
							vector<Action> actionsList = buildActionsList(location);
							auto t = getcommand(location, actionsList, passcode);
							location2 = get<0>(t);
							bool bools[5] = get<1>(t);
							victory = bools[4];
							fled = bools[3];
							TowerBeaten = bools[2];
							dead = bools[1];
							gamebeaten = bools[0];
							if (location != location2)
							{
								int pos = 0; //will need to be the index of locations where locations[pos].coords == location2
								cout << "pancakes" << endl; //will need to output locations[pos].description
								scan(location2);
							}
							location = location2;
							visitedlocations.push_back(location);
							if (location == [5, 9, -1])
							{
								dead, TowerBeaten, fled = true;
								victory = false;
								cout << "Before you have time to even realize where you are your systems suddenly shut down. It appears that your mission has ended just as soon as it has begun. GAME OVER\n\n" << endl;
							}
							else if (location == [0, 8, 0])
							{
								terminal(visitedlocations, location);
							}
							else if (location == [5, 9, 1])
							{
								fled, died = true;
							}
							else if (location == [-2, 2, 0])
							{
								dead, TowerBeaten, fled = true;
								victory = false;
							}
							else if ((location == [5, 7, 0]) && ([0, 8, 0] != [0, 2, 2])) //will eventually search for [0, 8, 0] in the list of game coords
							{
								cout << "There is a forcefield standing in the way between you and the tower. Until it isshut down, you shall not pass." << endl;
							}
						}
						else
						{
							location = [0, 0, 0];
							cout << "prologue" << endl;
						}
					}
					else
					{
						if (location == [5, 9, 1])
						{
							TowerBeaten = true;
							fled = false;
							//print midgame epilogue/prologue
						}
					}
				}
				while (towerBeaten)
				{
					if (!fled)
					{
						if (location != [1, 1, 1]) //will search list of valid game coordinates
						{
							vector<Action> actionsList = buildActionsList(location);
							auto t = getcommand(location, actionsList, passcode);
							location2 = get<0>(t);
							bool bools[5] = get<1>(t);
							victory = bools[4];
							fled = bools[3];
							TowerBeaten = bools[2];
							dead = bools[1];
							gamebeaten = bools[0];
							if (location != location2)
							{
								int pos = 0; //will need to be the index of locations where locations[pos].coords == location2
								cout << "pancakes" << endl; //will need to output locations[pos].description
								scan(location2);
							}
							location = location2;
							visitedlocations.push_back(location);
						}
						else
						{
							location = [0, 0, 0];
						}
					}
					else
					{
						TowerBeaten = NULL;
					}
				}
				if (TowerBeaten == NULL)
				{
					dead = true;
				}
			}
			gamebeaten = true;
		}
		if (victory == true)
		{
			cout << "epilogue" << endl; //will print epilogue
			cout << "congrats" << endl; //prints congratulatory message
		}
		cout << "credits" << endl; //prints end credits
		string input;
		cout << "Would you like to play again? (Type yes/no or y/n):  ";
		cin >> input;
		if (input == "y" || input == "yes")
		{
			fled, TowerBeaten, dead, gamebeaten = false;
			victory = true;
		}
		else
		{
			cout << "Goodbye! Play again soon..." << endl;
			gameover = true;
			exit(1);
		}
	}
	*/

	return 0;
}