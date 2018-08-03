// Program by Anthony Rolfe
// CS265, Grantham University
// Written in C++
// This program reads the data that is stored in a predefined file and then formats it
// into a more readable format for saving into the output file.

//Header info
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
	//Variable Declaration
	ifstream inData;
	ofstream outData;
	string firstName, lastName, department;
	double grossSalary, bonus, tax, distanceTraveled, travelTime, costCup, paycheck, averageSpeed, salesAmount;
	int cupsSold;

	//Open input and output files
	cout << "Loading Data from files..." << endl;
	inData.open("inData.txt");
	outData.open("outData.txt");
	cout << "Data loaded." << endl;

	//Set parameters for output file (numbers to 2 decimal places)
	outData << fixed << showpoint;
	outData << setprecision(2);

	//Load data from input file
	cout << "Processing first line of data...";
	inData >> firstName >> lastName >> department;
	cout << "done" << endl;
	cout << "Processing second line of data...";
	inData >> grossSalary >> bonus >> tax;	
	cout << "done" << endl;
	cout << "Processing third line of data...";
	inData >> distanceTraveled >> travelTime;
	cout << "done" << endl;
	cout << "Processing fourth line of data...";
	inData >> cupsSold >> costCup;
	cout << "done. All data inputted successfully." << endl;

	//Figure paycheck amount
	cout << "Processing Paycheck Info...";
	paycheck = grossSalary + (grossSalary * (bonus / 100)); // First add the bonus
	paycheck = paycheck - (paycheck * (tax / 100));  //Then deduct the taxes
	cout << "done" << endl;

	//Figure average speed
	cout << "Determining Average Speed....";
	averageSpeed = distanceTraveled / travelTime;
	cout << "done" << endl;

	//Figure sales amount
	cout << "Figuring Sales Amount...";
	salesAmount = cupsSold * costCup;
	cout << "done" << endl;

	//Write formatted data to output file
	cout << "Generating Output Report...";
	outData << "Name: " << firstName << " " << lastName << ", Department: " << department << endl;
	outData << "Monthly Gross Salary: " << grossSalary << ", Monthly Bonus: " << bonus << "%, Taxes: ";
	outData << tax << "%" << endl;
	outData << "Paycheck: $" << paycheck << endl;
	outData << endl;
	outData << "Distance Traveled: " << distanceTraveled << " miles. Travel Time: " << travelTime << " hours" << endl;
	outData << "Average Speed: " << averageSpeed << " mph" << endl;
	outData << "Number of Coffee Cups Sold: " << cupsSold << ", Cost: $" << costCup << " per cup" << endl;
	outData << "Sales Amount = $" << salesAmount << endl;
	cout << "done. Refer to outData.txt to see report info. Goodbye!" << endl;

	//Close files
	inData.close();
	outData.close();

	system("PAUSE");
	return 0;
}

