subtotal = 0
tax = 0
total = 0
print('Welcome to the Express Lane! You may now checkout five items.')
subtotal = subtotal + float(input('Enter the price of the first item: '))
subtotal = subtotal + float(input('Enter the price of the second item: '))
subtotal = subtotal + float(input('Enter the price of the third item: '))
subtotal = subtotal + float(input('Enter the price of the fourth item: '))
subtotal = subtotal + float(input('Enter the price of the final item: '))
tax = subtotal * .06
total = subtotal + tax
print('subtotal: ', format(subtotal, '.2f'))
print('sales tax: ', format(tax, '.2f'))
print('-------------------------')
print('total: ', format(total, '.2f'))
