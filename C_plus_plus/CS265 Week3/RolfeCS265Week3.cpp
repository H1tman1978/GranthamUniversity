// Program by Anthony Rolfe
// CS265, Grantham University
// Written in C++
// This program generates a cell phone bill based on input from the user. It will utilize the Windows console.

// Program Header Info
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std; 

//Program Functions
//Function for displaying the program menu
int displayMenu() {
	int selection;
	cout << "*****************MAIN MENU*****************" << endl;
	cout << "Please select one fo the following options:" << endl;
	cout << "1 - Input Bill Info" << endl;
	cout << "2 - Display Last Bill Created" << endl;
	cout << "3 - Save Bill to File" << endl;
	cout << "9 - Quit Program" << endl;
	cout << "-------------------------------------------" << endl;
	cout << "Which menu option do you choose? ";
	cin >> selection;
	cout << endl;
	return selection;
}


//Funcion for Displaying a formatted bill
int displayBill(int account, char accountType, double minutesUsed, double total) {
	string displayAccountType;
	switch (accountType)
	{
	case 'r':
	case 'R':
		displayAccountType = "Regular";
		break;
	case 'p':
	case 'P':
		displayAccountType = "Premium";
		break;
	default:
		displayAccountType = "Invalid Account Type";
		break;
	}
	cout << fixed << showpoint;
	cout << setprecision(2);
	cout << endl;
	cout << "                  Billing Report                    " << endl;
	cout << "****************************************************" << endl;
	cout << "Account: " << account << " Type: " << displayAccountType << endl;
	cout << "Minutes Used: " << minutesUsed << endl;
	cout << "Amount Due: $" << total << endl;
	cout << "****************************************************" << endl;
	cout << endl;
	return 0;
}

//Function for saving bill to a file
int saveBillToFile(int account, char accountType, double minutesUsed, double total)
{
	//Variable Declaration/Initialization
	string fileName;
	ofstream outFile;
	string displayAccountType;

	//Output formatting
	outFile << fixed << showpoint;
	outFile << setprecision(2);
	
	//Logic Code for displaying account type
	switch (accountType)
	{
	case 'r':
	case 'R':
		displayAccountType = "Regular";
		break;
	case 'p':
	case 'P':
		displayAccountType = "Premium";
		break;
	default:
		displayAccountType = "Invalid Account Type";
		break;
	}
	cout << "Please enter the filename you wish to save to. Be sure to include the file extension: ";
	cin >> fileName;
	cout << "Saving bill to " << fileName << endl;
	outFile.open(fileName);
	outFile << "****************************************************" << endl;
	outFile << "Account: " << account << " Type: " << displayAccountType << endl;
	outFile << "Minutes Used: " << minutesUsed << endl;
	outFile << "Amount Due: $" << total << endl;
	outFile << "****************************************************" << endl;
	cout << endl;
	outFile.close();
	cout << "Bill saved successfully." << endl;	
	return 0;
}
//End of Program Functions

int main() //Start of main program loop
{
	//Variable Declaration
	char serviceType=' ';
	int accountNumber=0, menuSelection;
	double minutesUsed=0.0, billTotal=0.0, offPeakMinutes, peakMinutes;
	bool running = true;
	
	//Program Loop
	while (running)
	{
		menuSelection = displayMenu();
		switch (menuSelection)
		{
		case 1:
			//Get input
			cout << "Enter the customer's account number: ";
			cin >> accountNumber;
			cout << endl;
			cout << "Enter \"R\" for Regular Account or \"P\" for Premium Account: ";
			cin >> serviceType;
			cout << endl;
			cout << "Enter the number of phone call minutes used: ";
			cin >> minutesUsed;
			cout << endl;

			//Logic Programming to determine Bill Total
			switch (serviceType)
			{
			case 'p':
			case 'P':
				//Premium service: $25.00 plus:
				//a.For calls made from 6:00 a.m.to 6 : 00 p.m., the first 75 minutes are free; 
				//charges for more than 75 minutes are $0.10 per minute.
				//b.For calls made from 6:00 p.m.to 6 : 00 a.m., the first 100 minutes are free; 
				//charges for more than 100 minutes are $0.05 per minute.
				billTotal = 25;  //Basic charge for Premium Service
				cout << "How many minutes were used during 6:00 pm to 6:00 am? ";
				cin >> offPeakMinutes;
				cout << endl;
				peakMinutes = minutesUsed - offPeakMinutes;
				if (peakMinutes > 75)
					billTotal += (peakMinutes - 75) * .10;
				if (offPeakMinutes > 100)
					billTotal += (offPeakMinutes - 100) * .05;
				break;
			case 'r':
			case 'R':
				//Regular service: $10.00 plus first 50 minutes are free. 
				//Charges for over 50 minutes are $0.20 per minute.
				billTotal = 10;
				if (minutesUsed > 50)
					billTotal += (minutesUsed - 50) * .2;
				break;
			default:
				cout << "Invalid input. Let's try again...";
				break;
			}
			break;
		case 2:
			displayBill(accountNumber, serviceType, minutesUsed, billTotal);
			break;
		case 3:
			saveBillToFile(accountNumber, serviceType, minutesUsed, billTotal);
			break;
		case 9:
			cout << "Thank you for using Tony's Automated Bill Generator. Goodbye!" << endl;
			running = false;
			break;
		default:
			cout << "Invalid selection. Please try again!" << endl;
			break;
		}
	}
	
	//Close the program
	system("PAUSE");
	return 0;
}