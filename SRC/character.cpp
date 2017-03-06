// character.cpp
#include "character.hpp"

void Character::print( ostream& out )
{
	out << "<player>" << m_name << "</player>";
}