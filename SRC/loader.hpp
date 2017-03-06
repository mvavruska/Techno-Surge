// load/update save files for game
#include <iostream>

class Loader
{
private:
	std::string fileName;

public:
	Loader() = default;
	void loadGame();
	void newGame();
	void autoSave();
};
