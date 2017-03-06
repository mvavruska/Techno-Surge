// Character.hpp
#include <string>;
using namespace std;

class Character
{
private:
	string m_name = "Buster";
	//Location m_pos;
public:
	Character() = default;
	//Character( Location p ) : m_pos( p ) { };

	void print( ostream& out );
};
