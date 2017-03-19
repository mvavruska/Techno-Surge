#pragma once
// Character.hpp
#include <string>;
// STRUCT FORWARD DECLARATION
struct Location;

class Character
{
private:
	std::string m_name = "Buster";
	Location *m_pos;
public:
	Character() = default;
	Character( Location* p ) : m_pos( p ) { };

	void print( std::ostream& out );
};
