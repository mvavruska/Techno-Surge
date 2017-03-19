// character.cpp
#include "character.hpp"

void Character::print( std::ostream& out )
{
	out << "<player>" << m_name << "</player>";
}