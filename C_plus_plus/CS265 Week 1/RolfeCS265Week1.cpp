// *******************************************************************************************
// Program by Anthony Rolfe
// CS265, Grantham University
// Written in C++
// This program averages three numbers and then displays the average. Numbers are hard-coded
// *******************************************************************************************

#include <iostream> //This line tells the computer which header(s) to use

using namespace std; //This line tells the computer to use standard input and output streams

int main() //Start of main program loop
{
	//Variable Declaration
	int num1, num2, num3, average;

	//Execution
	num1 = 125;								//This line stores 125 in variable num1
	num2 = 28;								//This line stores 28 in variable num2
	num3 = -25;								//This line stores -25 in variable num3
	average = (num1 + num2 + num3) / 3;		//This line performs the average of the 3 numbers

											//Output
	cout << "The average of your numbers is " << average << endl;	//This line displays the average as output
	system("PAUSE")
	return 0;		//This line signals the end of the function
}