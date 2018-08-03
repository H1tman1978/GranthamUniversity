// Program by Anthony Rolfe
// CS265, Grantham University
// Written in C++
// This program decodes an alphabetical phone number such as GOFEDEX (463-3339)

//Header info
#include <iostream> 
#include <string>
using namespace std; 

//Program functions
//This function converts a string to all caps. Thanks to Keith Nicholas on Stack Overflow
//for the code idea. https://stackoverflow.com/questions/8302797/convert-string-into-all-uppercase-c
void stringToUpper(string &s)
{
	for (unsigned int index = 0; index < s.length(); index++) 
	{
		s[index] = toupper(s[index]);
	}
}

//This funtion converts the alphabetic phone number into a numerical one
string phoneNumberDecoder(string countryCode, string areaCode, string letters) {
	//local variable declaration
	string decodedNumber, returnedNumber;
	letters.resize(7);  //Trims the inputted letters to the first 7 letters (this is what phone companies do)
	decodedNumber = letters;  //Initialize decodedNumber as a copy of letters
	//Execution
	stringToUpper(letters); //To make sure that the letters are all upper-case
	for (int i = 0; i < 7; i++) {
		switch (letters[i]) {
		    case 'A':
		    case 'B':
		    case 'C':
			    decodedNumber[i] = '2';
			    break;
		    case 'D':
		    case 'E':
		    case 'F':
			    decodedNumber[i] = '3';
			    break;
		    case 'G':
		    case 'H':
		    case 'I':
			    decodedNumber[i] = '4';
			    break;
		    case 'J':
		    case 'K':
		    case 'L':
			    decodedNumber[i] = '5';
			    break;
		    case 'M':
		    case 'N':
		    case 'O':
			    decodedNumber[i] = '6';
			    break;
		    case 'P':
		    case 'Q':
		    case 'R':
		    case 'S':
			     decodedNumber[i] = '7';
			     break;
		    case 'T':
		    case 'U':
		    case 'V':
			    decodedNumber[i] = '8';
			    break;
		    case 'W':
		    case 'X':
		    case 'Y':
		    case 'Z':
			    decodedNumber[i] = '9';
			    break;
			//the default will simply copy it over (in case there is a number mixed with the letters)
		    default:
			    decodedNumber[i] = letters[i];
			    break;
		} //End of Switch Statement
		
	} //End of for loop
	//Format the decoded phone number
	returnedNumber = "+" + countryCode + "(" + areaCode + ")" + decodedNumber;
	return returnedNumber;
}	//End of phoneNumberDecoder

//This function  obtains the country code of the number to be decoded
string getCountryCode() {
	//Local Variable Declaration
	string countryCode;

	//Execution
	cout << "Please enter the country code (USA, Can, Mex = 1) of the phone number you wish to decode: ";
	cin >> countryCode;
	return countryCode;
}

//This function obtains the area code from the user
string getAreaCode() {
	//Local Variable Declaration
	string areaCode;
	cout << "Please enter the area code: ";
	cin >> areaCode;
	return areaCode;
}

//This function obtains the rest of the phone number
string getCodedNumber() {
	//Local Variable Declaration
	string codedNumber;

	//Execution
	cout << "Please enter the rest of the number that needs decoding: ";
	cin >> codedNumber;	
	return codedNumber;
}
// End of program functions

int main() //Start of main program loop
{
	//Variable Declaration
	string countryCode, areaCode, letterNumber, decodedNumber;
	char decodeAgain;
	bool running = true;

	//Program Initialization
	cout << "Welcome to Phone Number Decoder 1.0!" << endl;
	do	{
		//Input from User		
		countryCode = getCountryCode();
		areaCode = getAreaCode();
		letterNumber = getCodedNumber();

		//Execution
		decodedNumber = phoneNumberDecoder(countryCode, areaCode, letterNumber);

		//Output		
		cout << "Your decoded phone number is " << decodedNumber << "." << endl;
		cout << "Do you wish to decode another number, y/n? ";
		cin >> decodeAgain;
		cout << endl;
		if (decodeAgain == 'y' || decodeAgain == 'Y')
			continue;
		else //Any thing besides a 'y' or 'Y' will be treated as a no.
			running = false;
	} while (running); //Program Loop
	
	//Close the program
	cout << endl;
	cout << "Thank you for using Phone Decoder 1.0" << endl;
	system("PAUSE");
	return 0;
}	//End of main program 
