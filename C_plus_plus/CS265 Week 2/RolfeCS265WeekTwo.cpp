// Program by Anthony Rolfe
// CS265, Grantham University
// Written in C++
// This program reads the data that is stored in a predefined file and then formats it
// into a more readable format for saving into the output file.

//Header info
#include "stdafx.h"
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
	cout << "Loading Data from files...";
	inData.open("inData.txt");
	outData.open("outData.txt");
	cout << "Data loaded.";

	//Set parameters for output file (numbers to 2 decimal places)
	outData << fixed << showpoint;
	outData << setprecision(2);

	//Load data from input file
	inData >> firstName >> lastName >> department;
	inData >> grossSalary >> bonus >> tax;

	//debug code
	cout << grossSalary << " " << bonus << " " << tax;
	inData >> distanceTraveled >> travelTime;
	inData >> cupsSold >> costCup;

	//Figure paycheck amount
	paycheck = grossSalary + (grossSalary * (bonus / 100)); // First add the bonus
	paycheck = paycheck - (paycheck * (tax / 100));  //Then deduct the taxes

													 //Figure average speed
	averageSpeed = distanceTraveled / travelTime;

	//Figure sales amount
	salesAmount = cupsSold * costCup;

	//Write formatted data to output file
	outData << "Name: " << firstName << " " << lastName << ", Department: " << department << endl;
	outData << "Monthly Gross Salary: " << grossSalary << ", Monthly Bonus: " << bonus << "%, Taxes: ";
	outData << tax << "%" << endl;
	outData << "Paycheck: $" << paycheck << endl;
	outData << endl;
	outData << "Distance Traveled: " << distanceTraveled << " miles. Travel Time: " << travelTime << " hours" << endl;
	outData << "Average Speed: " << averageSpeed << " mph" << endl;
	outData << "Number of Coffee Cups Sold: " << cupsSold << ", Cost: $" << costCup << " per cup" << endl;
	outData << "Sales Amount = $" << salesAmount << endl;

	//Close files
	inData.close();
	outData.close();

	system("PAUSE");
	return 0;
}

