// load/update save files for game
#include <iostream>

class Loader
{
private:
	std::string fileName;

public:
	Loader() = default;
	static void newGame();
	static void loadGame();
	static void autoSave();
	static void saveGame();
};
