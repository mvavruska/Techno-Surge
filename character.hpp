// Character.hpp

class Character
{
private:
	Location m_pos;
public:
	Character() = default;
	Character( Location p ) : m_pos( p ) { };
};