print('Welcome to Tonys Payrole Management Program') #Introduction to Program

#Declaration of Variables
name = ''
hoursWorked = 0.00
overtimeHours = 0.00
normalhours = 0.00
payrate = 0.00
grosspay = 0.00
overtimePay = 0.00
normalPay = 0.00

#Program Loop
while name != 'q' :

   #Get Input
   name = input('Enter employee\'s name or \"q\" to quit: ')
   if name == 'q': break #Used to quit loop
   hoursWorked = float(input('Enter hours worked: '))
   payrate = float(input('Enter employee\'s payrate: '))

   #Calculate Grosspay
   if hoursWorked > 40 :
      normalhours = 40
      overtimeHours = hoursWorked - 40
   else :
      normalhours = hoursWorked
      overtimeHours = 0
   normalPay = normalhours * payrate
   overtimePay = overtimeHours * (payrate * 1.5)
   grosspay = normalPay + overtimePay

   #output Name, Gross Pay and Overtime pay if applicable
   if overtimeHours > 0:
       print('Employee Name:  ', name)
       print('Grosspay:  ', format(grosspay, '.2f'))
       print('(overtime pay: ', format(overtimePay, '.2f'), '\b)')
   else :
       print ('Employee Name:  ', name)
       print('Grosspay:  ', format(grosspay, '.2f'))
print ('Goodbye!')#This lets the user know that the program has successfully terminated.