#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string fileToString( string );			// read file as string
string reformatString( string );		// reformat string to specific format
string removeChar( string, char );		// remove a specific char from string
void writeFile( string, string );		// write reformatted text to file

int
main()
{
	string contents = fileToString( "input.txt" );
	string newText = reformatString( contents );
	writeFile( newText, "output.txt" );
    return 0;
}

string
fileToString( string fileName )
{
	ifstream read( fileName );
	string contents = "", line;
	while( read.good() )
	{
		getline( read, line );
		contents += line;
	}
	read.close();
	return contents;
}

// per block:
// CONVERT """ string text here """ [ -1, 0, 2 ] TO [-1,0,2] string text here
string
reformatString( string content )
{
	string result = "";
	int start = 0, stringEnd, end;
	string block, dialog, coord;
	// per block
	while( content.find( "\"\"\"", start ) != -1 )
	{
		start = content.find( "\"\"\"", start );
		stringEnd = content.find( "\"\"\"", start + 1 );
		end = content.find( "]", stringEnd );
		//cout << start << " " << stringEnd << " " << end << endl;
		block = content.substr( start + 3, end - ( start + 2 ));
		cout << block << endl;
		stringEnd = stringEnd - start; // redefine stringEnd to be in block
		
		dialog = block.substr( 0, stringEnd - 3 );
		dialog = removeChar( dialog, '\\' );
		coord = block.substr( stringEnd + 2, block.length() - stringEnd - 1 );
		coord = removeChar( coord, ' ' );

		cout << coord << " " << dialog << endl;

		result += "\n" + coord + " " + dialog;
		start = end + 1;
	}
	return result;
}

string
removeChar( string text, char z )
{
	string newText = "";
	for( char c : text ) newText += ( c == z ? "" : string( 1, c ));
	return newText;
}

void
writeFile( string content, string fileName )
{
	ofstream out( fileName );
	out << content;
	out.close();
}