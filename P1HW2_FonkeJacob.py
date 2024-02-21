#Jacob Fonke
#2/21/24
#P1HW2
#Travel Expenses

'''Ask user to enter their budget
Ask user to enter travel destination
Ask user for amount they will spend on gas
Ask user for amount they will spend on accommodation
Ask user for amount they will spend on food
Add expenses
Subtract expenses from budget
Display results'''

print("This program calculates and displays travel expenses")

budget = int(input("Enter Budget:"))

dest = input("Enter your travel destination:")

gas_cost = int(input("How much do you think you will spend on gas?"))

hotel_cost = int(input("Approximately, how much will you need for accomodation/hotel?"))

food_cost = int(input("Last, how much do you need for food?"))

print("----------Travel Expenses----------")

print("Location:", dest)
print("Initial Budget:", budget)

print("Fuel:", gas_cost)
print("Accomodation:", hotel_cost)
print("Food:", food_cost)

remaining_bal = budget - gas_cost - hotel_cost - food_cost
print("Remaining Balance:", remaining_bal)
